from flask import Blueprint, redirect, request, jsonify, session, render_template
from Config.db import app, db, ma
from Models.PrestamoDetalle import PrestamoDetalle, PrestamoDetalleSchema

ruta_prestamodetalle = Blueprint("routes_prestamodetalle", __name__)

prestamodetalle_schema   = PrestamoDetalleSchema()
prestamodetalles_schemas = PrestamoDetalleSchema(many=True)

@ruta_prestamodetalle.route('/prestamoDetalle', methods=['GET'])
def PrestamoDetalle():
    resultall = PrestamoDetalle.query.all()
    resultPrestamodetalles = prestamodetalles_schemas.dump(resultall)
    return jsonify(resultPrestamodetalles)