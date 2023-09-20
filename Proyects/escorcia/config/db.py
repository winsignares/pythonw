from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.environ.get('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
or 'sqlite:///' + os.path.join(basedir, 'loans.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFACATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

app.secret_key = SECRET_KEY

db = SQLAlchemy(app)
ma = Marshmallow(app)