from flask import Blueprint, redirect, request, jsonify, session, render_template
from Config.db import app, db, ma
from Models.Detalle_prestamo import DetallePrestamo, DetallePrestamoSchema

ruta_detalle_prestamo = Blueprint("routes_detalles_prestamo", __name__)

detalle_prestamo_schema  = DetallePrestamoSchema()
detalle_prestamo_schemas = DetallePrestamoSchema(many=True)

@ruta_detalle_prestamo.route('/detalle_prestamos', methods=['GET'])
def clientes():
    results = DetallePrestamo.query.all()

    return jsonify(detalle_prestamo_schemas.dump(results))
