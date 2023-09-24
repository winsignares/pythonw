from flask import Blueprint, redirect, request, jsonify, session, render_template
from Config.db import app, db, ma
from Models.Prestamista import Prestamista, PrestamistaSchema

ruta_prestamista = Blueprint("routes_prestamista", __name__)

prestamista_schema   = PrestamistaSchema()
prestamistas_schemas = PrestamistaSchema(many=True)

@ruta_prestamista.route('/prestamistas', methods=['GET'])
def prestamistas():
    resultall = Prestamista.query.all()
    resultprestamistas = prestamistas_schemas.dump(resultall)
    return jsonify(resultprestamistas)