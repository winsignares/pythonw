from flask import Blueprint, request, jsonify
from config.db import db, ma
from Models.Pago import Pago, PagoSchema
from datetime import date

ruta_pago = Blueprint("routes_pago", __name__)

pago_schema = PagoSchema()
pagos_schema = PagoSchema(many=True)

@ruta_pago.route('/pagos', methods=['GET', 'POST'])
def obtener_pagos():
    if request.method == 'GET':
        pagos = Pago.query.all()
        resultado = pagos_schema.dump(pagos)
        return jsonify(resultado)
    
    if request.method == 'POST':
        
        id_prestamo = request.json['id_prestamo']
        fecha_pago = date.fromisoformat(request.json['fecha_pago'])
        monto_pago = request.json['monto_pago']
        numero_cuota = request.json['numero_cuota']

        nuevo_pago = Pago(id_prestamo=id_prestamo, fecha_pago=fecha_pago, monto_pago=monto_pago, numero_cuota=numero_cuota)

        db.session.add(nuevo_pago)
        db.session.commit()

        return pago_schema.jsonify(nuevo_pago)