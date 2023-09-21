from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db import app, db, ma
from models.prestamista import Prestamistas, PrestamistasSchema

ruta_prestamistas = Blueprint("routes_prestamita", __name__)

prestamista_schema   = PrestamistasSchema()
prestamistas_schemas = PrestamistasSchema(many=True)

@ruta_prestamistas.route('/prestamistas', methods=['GET'])
def prestamistas():
    resultall = Prestamistas.query.all()
    resultPrestamistas = prestamistas_schemas.dump(resultall)
    return jsonify(resultPrestamistas)
