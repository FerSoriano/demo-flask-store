from os import environ
from werkzeug.security import check_password_hash
from peewee import IntegrityError, DoesNotExist
from database import User, Product
from flask import (
    Flask,
    render_template,
    request, session,
    redirect,
    url_for,
    abort
)

app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password:
            try:
                user = User.create_user(username, password)
                session['user_id'] = user.id
                return redirect(url_for('products'))
            except IntegrityError:
                error = 'Username already exists. Try again.'

    return render_template('register.html', error=error)


@app.route('/products')
def products():
    user = User.get(session['user_id'])
    _products = user.products
    return render_template('products/index.html', products=_products)


@app.route('/products/create', methods=['GET', 'POST'])
def create_products():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')

        if name and price:
            user = User.get(session['user_id'])
            Product.create(name=name, price=price, user=user)
            return redirect(url_for('products'))

    return render_template('products/create.html')


@app.route('/products/update/<id>', methods=['GET', 'POST'])
def update_products(id: int):
    error = None
    try:
        product = Product.get_by_id(id)
    except DoesNotExist:
        abort(404)

    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')

        if name and price:
            Product.update(
                name=name,
                price=price
            ).where(Product.id == id).execute()

            return redirect(url_for('products'))
        else:
            error = 'Need to fill both fields'

    return render_template('products/update.html',
                           product=product,
                           error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.select().where(User.username == username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('products'))
        else:
            error = "Invalid Credentials. Try Again."

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))


if __name__ == '__name__':
    app.run(debug=True, load_dotenv=True)
