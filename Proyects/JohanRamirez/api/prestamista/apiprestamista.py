from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db import app, db, ma
from models.prestamista import Prestamista, PrestamistaSchema

ruta_prestamista = Blueprint("routes_prestamista", __name__)

prestamista_schema   = PrestamistaSchema()
prestamista_schemas = PrestamistaSchema(many=True)

@ruta_prestamista.route('/prestamistas', methods=['GET'])
def clientes():
    resultall = Prestamista.query.all()
    resultPrestamistas = prestamista_schemas.dump(resultall)
    return jsonify(resultPrestamistas)