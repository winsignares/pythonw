from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db import app, db, ma
from Models.Prestamo import Prestamo, PrestamoSchema
from datetime import date

ruta_prestamo = Blueprint("routes_prestamo", __name__)

prestamo_schema   = PrestamoSchema()
prestamos_schemas = PrestamoSchema(many=True)

@ruta_prestamo.route('/prestamo', methods=['GET', 'POST', 'PUT'])
def clientes():
    if request.method == 'GET':
        resultall = Prestamo.query.all()
        resultPrestamo = prestamos_schemas.dump(resultall)
        return jsonify(resultPrestamo)
    
    if request.method == 'POST':
        id_cliente = request.json['id_cliente']
        prestamista_id = request.json['prestamista_id']
        monto_prestamo = request.json['monto_prestamo']
        fecha_inicio = date.fromisoformat(request.json['fecha_inicio'])
        fecha_finalizacion = date.fromisoformat(request.json['fecha_finalizacion'])
        tasa_interes = request.json['tasa_interes']
        estado_prestamo = "Pendiente"
        cuotas_pendientes = request.json['cuotas_pendientes']

        nuevo_prestamo = Prestamo(id_cliente=id_cliente, prestamista_id=prestamista_id, monto_prestamo=monto_prestamo, fecha_inicio=fecha_inicio, fecha_finalizacion=fecha_finalizacion, tasa_interes=tasa_interes, estado_prestamo=estado_prestamo, cuotas_pendientes=cuotas_pendientes)

        db.session.add(nuevo_prestamo)
        db.session.commit()

        return prestamo_schema.jsonify(nuevo_prestamo)
        
    
    if request.method == 'PUT':
        id = request.json['id']
        estado = request.json['estado']
        prestamo = Prestamo.query.get(id)
        prestamo.estado = estado
        db.session.commit()
        return prestamo_schema.jsonify(prestamo)
