from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db import app, db, ma
from models.prestamo_detalle import Prestamos_detalle, Prestamos_detalleSchema

ruta_prestamosdetalle = Blueprint("routes_prestamodetalle", __name__)

prestamodetalle_schema   = Prestamos_detalleSchema()
prestamodetalles_schemas = Prestamos_detalleSchema(many=True)

@ruta_prestamosdetalle.route('/prestamos_detalle', methods=['GET'])
def clientes():
    resultall = Prestamos_detalle.query.all()
    resultPrestamodetalles = prestamodetalles_schemas.dump(resultall)
    return jsonify(resultPrestamodetalles)
