from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()
app = Flask(__name__)

#creamos las credenciales para conectarnos a la bd

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:familiab2@localhost/prestamoul'

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}/{os.environ['DB_NAME']}"

app.config['SQLALCHEMY_TRACK_MODIFACATIONS'] = False

app.secret_key = "WebAvanzada"

#creamos los objetos de bd

db = SQLAlchemy(app)
ma = Marshmallow(app)