from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db import app, db, ma
from Models.Cliente import Cliente, ClienteSchema

ruta_cliente = Blueprint("routes_cliente", __name__)

cliente_schema   = ClienteSchema()
clientes_schemas = ClienteSchema(many=True)

@ruta_cliente.route('/clientes', methods=['GET', 'POST', 'DELETE'])
def clientes():
    if request.method == 'GET':
        resultall = Cliente.query.all()
        resultClientes = clientes_schemas.dump(resultall)
        return jsonify(resultClientes)
    
    if request.method == 'POST':
        id = request.json['id']
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        direccion = request.json['direccion']
        telefono = request.json['telefono']
        correo_electronico = request.json['correo_electronico']

        nuevo_cliente = Cliente(id=id, nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono,correo_electronico=correo_electronico)

        db.session.add(nuevo_cliente)
        db.session.commit()

        return cliente_schema.jsonify(nuevo_cliente)
    
    if request.method == 'DELETE':
        id = request.json['id']
        cliente = Cliente.query.get(id)
        db.session.delete(cliente)
        db.session.commit()
        return cliente_schema.jsonify(cliente)
