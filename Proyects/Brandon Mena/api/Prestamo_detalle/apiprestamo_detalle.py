from flask import Blueprint, redirect, request, jsonify, session, render_template
from Config.db import app, db, ma
from Models.Prestamo_detalle import Prestamo_detalle, Prestamo_detalleSchema

ruta_prestamodetalle = Blueprint("routes_prestamodetalle", __name__)

prestamodetalle_schema   = Prestamo_detalleSchema()
prestamodetalles_schemas = Prestamo_detalleSchema(many=True)

@ruta_prestamodetalle.route('/prestamo_detalle', methods=['GET'])
def clientes():
    resultall = Prestamo_detalle.query.all()
    resultPrestamodetalles = prestamodetalles_schemas.dump(resultall)
    return jsonify(resultPrestamodetalles)
