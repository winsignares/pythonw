from flask import Blueprint, request, jsonify
from config.db import db, ma
from Models.Prestamista import Prestamista, PrestamistaSchema

ruta_prestamista = Blueprint("routes_prestamista", __name__)

prestamista_schema = PrestamistaSchema()
prestamistas_schema = PrestamistaSchema(many=True)

@ruta_prestamista.route('/prestamistas', methods=['GET', 'POST', 'DELETE'])
def obtener_prestamistas():
    if request.method == 'GET':
        prestamistas = Prestamista.query.all()
        resultado = prestamistas_schema.dump(prestamistas)
        return jsonify(resultado)
    
    if request.method == 'POST':
        id = request.json['id']
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        direccion = request.json['direccion']
        telefono = request.json['telefono']
        correo_electronico = request.json['correo_electronico']

        nuevo_prestamista = Prestamista(id=id, nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono,correo_electronico=correo_electronico)

        db.session.add(nuevo_prestamista)
        db.session.commit()

        return prestamista_schema.jsonify(nuevo_prestamista)
    
    if request.method == 'DELETE':
        id = request.json['id']
        prestamista = Prestamista.query.get(id)
        db.session.delete(prestamista)
        db.session.commit()
        return prestamista_schema.jsonify(prestamista)