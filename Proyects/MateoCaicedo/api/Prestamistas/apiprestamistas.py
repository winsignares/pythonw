from flask import Blueprint, redirect, request, jsonify, session, render_template
from Config.db import app, db, ma
from Models.Prestamista import Prestamista, PrestamistaSchema

ruta_prestamistas = Blueprint("routes_prestamistas", __name__)

prestamistas_schema   = PrestamistaSchema()
prestamistas_schemas = PrestamistaSchema(many=True)

@ruta_prestamistas.route('/prestamistas', methods=['GET'])
def clientes():
    resultall = Prestamista.query.all()
    results = prestamistas_schemas.dump(resultall)
    return jsonify(results)
