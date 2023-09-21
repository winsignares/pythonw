from flask import Flask, request, jsonify, redirect, render_template
from Config.db import app
from api.Cliente.apiclientes import ruta_cliente
from api.Prestamo.apiprestamos import ruta_prestamo
from api.Detalles_prestamo import ruta_detalles_prestamo
from api.Prestamista import ruta_prestamista

app.register_blueprint(ruta_cliente, url_prefix = "/api" )
app.register_blueprint(ruta_prestamista, url_prefix = "/api")
app.register_blueprint(ruta_prestamo, url_prefix = "/api" )
app.register_blueprint(ruta_detalles_prestamo, url_prefix = "/api" )


@app.route("/")
def index():
    return "Andres Barrios"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')