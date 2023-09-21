from flask import Blueprint, redirect, request, jsonify, session, render_template
from Config.db import app, db, ma
from Models.DetallePrestamo import DetallePrestamo, DetallePrestamoSchema

ruta_detalle_prestamo = Blueprint("routes_detalle_prestamo", __name__)

detalle_prestamo_schema   = DetallePrestamoSchema()
detalle_prestamos_schemas = DetallePrestamoSchema(many=True)

@ruta_detalle_prestamo.route('/detalle_prestamos', methods=['GET'])
def clientes():
    resultall = DetallePrestamo.query.all()
    resultDetallePrestamo = detalle_prestamos_schemas.dump(resultall)
    return jsonify(resultDetallePrestamo)
