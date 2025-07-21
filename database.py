from os import environ
from datetime import datetime
from werkzeug.security import generate_password_hash
from peewee import (
    MySQLDatabase,
    Model,
    CharField,
    DateTimeField,
    TextField,
    IntegerField,
    ForeignKeyField
)

DB_CONFIG = {
    'database': environ.get('DB_NAME',),
    'user': environ.get('DB_USER'),
    'password': environ.get('DB_PASSWORD'),
    'host': environ.get('DB_HOST'),
    'port': int(environ.get('DB_PORT'))
}

db = MySQLDatabase(**DB_CONFIG)


class User(Model):
    username = CharField(unique=True)
    password = CharField()
    created_at = DateTimeField(default=datetime.now())

    class Meta:
        database = db
        db_table = 'users'

    @classmethod
    def create_user(cls, _username, _password):
        _password = generate_password_hash(_password)  # f'cody_{_password}'
        return cls.create(username=_username, password=_password)


class Product(Model):
    name = TextField()
    price = IntegerField()
    user = ForeignKeyField(User, backref='products')
    created_at = DateTimeField(default=datetime.now())

    class Meta:
        database = db
        db_table = 'products'

    @property  # cambia la propiedad del elemento, no afecta al registro de la base de datos  # noqa
    def price_format(self):
        return f'${self.price} dollars'


db.connect()
db.create_tables([User, Product])
print("¡Tablas creadas correctamente!")
