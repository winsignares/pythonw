from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

#creamos las credenciales para conectarnos a la bd


app.secret_key = "WebAvanzada"

#creamos los objetos de bd