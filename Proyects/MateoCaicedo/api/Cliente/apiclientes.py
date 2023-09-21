from flask import Blueprint, request, jsonify
from Config.db import app, db, ma
from Models.Cliente import Cliente, ClienteSchema

ruta_cliente = Blueprint("routes_cliente", __name__)

cliente_schema   = ClienteSchema()
clientes_schemas = ClienteSchema(many=True)

@ruta_cliente.route('/clientes', methods=['GET'])
def clientes():
    resultall = Cliente.query.all()
    resultClientes = clientes_schemas.dump(resultall)
    return jsonify(resultClientes)

# post

@ruta_cliente.route('/clientes', methods=['POST'])
def create_cliente():
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    direccion = request.json['direccion']
    telefono = request.json['telefono']
    email = request.json['email']

    new_cliente = Cliente(nombre, apellido, direccion, telefono, email)

    db.session.add(new_cliente)
    db.session.commit()

    return cliente_schema.jsonify(new_cliente)