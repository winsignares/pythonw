from flask import Flask, request, jsonify, redirect, render_template
from config.db import app
from api.cliente.apiclientes import ruta_cliente
from api.prestamo.apiprestamos import ruta_prestamo
from api.detallesPrestamo.apidetalles_prestamo import ruta_detalles_prestamo
from api.prestamista.apiprestamista import ruta_prestamista


app.register_blueprint(ruta_cliente, url_prefix = "/api" )
app.register_blueprint(ruta_prestamo, url_prefix = "/api" )
app.register_blueprint(ruta_detalles_prestamo, url_prefix = "/api" )
app.register_blueprint(ruta_prestamista, url_prefix = "/api" )




@app.route("/")
def index():
    return "Hola Mundo Johan"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')