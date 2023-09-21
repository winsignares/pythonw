from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db import app, db, ma
from models.prestamo import Prestamos, PrestamosSchema

ruta_prestamos = Blueprint("routes_prestamo", __name__)

prestamo_schema   = PrestamosSchema()
prestamos_schemas = PrestamosSchema(many=True)

@ruta_prestamos.route('/prestamos', methods=['GET'])
def clientes():
    resultall = Prestamos.query.all()
    resultPrestamo = prestamos_schemas.dump(resultall)
    return jsonify(resultPrestamo)
