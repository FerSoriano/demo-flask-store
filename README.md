# 🛒 Tienda Online

Este proyecto es una aplicación web simple de una tienda en línea desarrollada con **Flask**, **Python** y **MySQL**. Es un proyecto personal creado con fines educativos para practicar los conceptos de Backend con Python.

## 🚀 Características

- Sistema de autenticación de usuarios:
  - Registro
  - Inicio de sesión
  - Cierre de sesión
- Administración de productos:
  - Crear productos asociados a un usuario
  - Editar productos
  - Eliminar productos
- Conexión a base de datos MySQL utilizando **Peewee ORM**
- Interfaz frontend con **HTML**, **CSS** y **Tailwind CSS**

## 🧱 Tecnologías utilizadas

### Backend

- Python
- Flask
- MySQL
- Peewee (ORM)
- PyMySQL
- python-dotenv

### Frontend

- HTML
- CSS
- Tailwind CSS

## 📦 Librerías utilizadas

```text
blinker==1.6.2
click==8.1.6
Flask==2.3.2
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
peewee==3.16.2
PyMySQL==1.1.1
python-dotenv==1.0.0
Werkzeug==2.3.6
```

## 🗄️ Modelos

- **User**: representa a los usuarios registrados en el sistema.
- **Product**: representa los productos creados por los usuarios. Cada producto está asociado a un usuario.

## ⚙️ Cómo ejecutar el proyecto

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/FerSoriano/demo-flask-store.git
   ```
2. **Crea y activa un entorno virtual**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En macOS/Linux
   .venv\Scripts\activate     # En Windows
   ```
3. **Insatala Dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Crea un archivo `.env` con tus variables de entorno**:
   Ejemplo:
   ```env
    SECRET_KEY=supersecretkey123
    DB_NAME=store
    DB_USER=root
    DB_PASSWORD=root
    DB_PORT=3306
    DB_HOST=localhost
   ```
5. **Asegurate de tener creada la base de datos en MySQL**:
   ```sql
   CREATE DATABASE demo_store;
   ```
6. **Ejecuta la app**:
   ```bash
   flask run
   ```
