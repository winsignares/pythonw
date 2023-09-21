from flask import Blueprint, redirect, request, jsonify, session, render_template
from config.db import app, db, ma
from models.cliente import Clientes, ClientesSchema

ruta_clientes = Blueprint("routes_cliente", __name__)

cliente_schema   = ClientesSchema()
clientes_schemas = ClientesSchema(many=True)

@ruta_clientes.route('/clientes', methods=['GET'])
def clientes():
    resultall = Clientes.query.all()
    resultClientes = clientes_schemas.dump(resultall)
    return jsonify(resultClientes)
