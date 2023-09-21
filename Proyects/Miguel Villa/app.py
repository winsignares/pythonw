from flask import Flask, request, jsonify, redirect, render_template
from config.db import app
from api.cliente.apiclientes import ruta_clientes
from api.prestamista.apiprestamistas import ruta_prestamistas
from api.prestamo.apiprestamos import ruta_prestamos
from api.prestamo_detalle.apiprestamos_detalle import ruta_prestamosdetalle



app.register_blueprint(ruta_clientes, url_prefix = "/api" )
app.register_blueprint(ruta_prestamistas, url_prefix = "/api")
app.register_blueprint(ruta_prestamos, url_prefix = "/api" )
app.register_blueprint(ruta_prestamosdetalle, url_prefix = "/api" )

@app.route("/")
def index():
    return "Hola Mundo Miguel Villa"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')