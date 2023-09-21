from flask import Blueprint, redirect, request, jsonify, session, render_template
from Config.db import app, db, ma
from Models.Detalle_Prestamo import Detalle_Prestamo, Detalle_PrestamoSchema

ruta_Detalle_Prestamo = Blueprint("routes_Detalle_Prestamo", __name__)

Detalle_Prestamo_schema   = Detalle_PrestamoSchema()
Detalle_Prestamos_schemas = Detalle_PrestamoSchema(many=True)

@ruta_Detalle_Prestamo.route('/Detalle_Prestamo', methods=['GET'])
def clientes():
    resultall = Detalle_Prestamo.query.all()
    resultDetalle_Prestamo = Detalle_Prestamos_schemas.dump(resultall)
    return jsonify(resultDetalle_Prestamo)