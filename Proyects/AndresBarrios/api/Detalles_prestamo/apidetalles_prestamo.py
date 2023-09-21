from flask import Blueprint, redirect, request, jsonify, session, render_template
from Config.db import app, db, ma
from Models.detalles_prestamo import Detalles_prestamo, DetallesPrestamoSchema

ruta_detalles_prestamo = Blueprint("routes_detalles_prestamo", __name__)

detalles_prestamo_schema   = DetallesPrestamoSchema()
detalles_prestamos_schemas = DetallesPrestamoSchema(many=True)

@ruta_detalles_prestamo.route('/detallesprestamos', methods=['GET'])
def clientes():
    resultall = Detalles_prestamo.query.all()
    resultPrestamo = detalles_prestamos_schemas.dump(resultall)
    return jsonify(resultPrestamo)