from flask import Blueprint, redirect, request, jsonify, session, render_template
from Config.db import app, db, ma
from Models.Prestamista import Prestamista, PrestamistaSchema

ruta_Prestamista = Blueprint("routes_Prestamista", __name__)

Prestamista_schema   = PrestamistaSchema()
Prestamistas_schemas = PrestamistaSchema(many=True)

@ruta_Prestamista.route('/Prestamistas', methods=['GET'])
def Prestamistas():
    resultall = Prestamista.query.all()
    resultPrestamistas = Prestamistas_schemas.dump(resultall)
    return jsonify(resultPrestamistas)