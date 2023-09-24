from flask import Blueprint, redirect, request, jsonify, session, render_template
from Config.db import app, db, ma
from Models.DetPrestamo import DetPrestamo, DetPrestamoSchema

ruta_detPrestamo = Blueprint("routes_detPrestamo", __name__)

detPrestamo_schema   = DetPrestamoSchema()
detPrestamos_schemas = DetPrestamoSchema(many=True)

@ruta_detPrestamo.route('/detPrestamos', methods=['GET'])
def detPrestamo():
    resultall = DetPrestamo.query.all()
    resultDetPrestamo = detPrestamos_schemas.dump(resultall)
    return jsonify(resultDetPrestamo)