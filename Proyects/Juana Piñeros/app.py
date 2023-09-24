from flask import Flask, request, jsonify, redirect, render_template
from Config.db import app
from api.Cliente.apiclientes import ruta_cliente
from api.Pestamista.apiprestamistas import ruta_prestamista
from api.Prestamo.apiprestamos import ruta_prestamo
from api.DetPrestamo.apidetprestamo import ruta_detPrestamo


app.register_blueprint(ruta_cliente, url_prefix = "/api" )
app.register_blueprint(ruta_prestamista, url_prefix = "/api" )
app.register_blueprint(ruta_prestamo, url_prefix = "/api" )
app.register_blueprint(ruta_detPrestamo, url_prefix = "/api" )

@app.route("/")
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')