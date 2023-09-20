from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db import app, db, ma
from models.cliente import Cliente, ClienteSchema

ruta_cliente = Blueprint("routes_cliente", __name__)

cliente_schema   = ClienteSchema()
clientes_schemas = ClienteSchema(many=True)

@ruta_cliente.route('/clientes', methods=['GET'])
def clientes():
    resultall = Cliente.query.all()
    resultClientes = clientes_schemas.dump(resultall)
    return jsonify(resultClientes)