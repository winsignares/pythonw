from flask import Blueprint, redirect, request, jsonify, session, render_template
from Config.db import app, db, ma
from Models.Prestamista import Prestamista, PrestamistaSchema

ruta_prestamista = Blueprint("routes_prestamista", __name__)
Prestamista_schema   = PrestamistaSchema()
Prestamistas_schemas = PrestamistaSchema(many=True)

@ruta_prestamista.route('/prestamista', methods=['GET'])
def Prestamistas():
    resultall = Prestamista.query.all()
    resultPrestamistas = Prestamistas_schemas.dump(resultall)
    return jsonify(resultPrestamistas)