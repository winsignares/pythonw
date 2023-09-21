from flask import Flask, request, jsonify, redirect, render_template
from Config2.db import app
from api2.Cliente.apiclientes import ruta_cliente
from api2.Prestamo.apiprestamos import ruta_prestamo

app.register_blueprint(ruta_cliente, url_prefix = "/api" )
app.register_blueprint(ruta_prestamo, url_prefix = "/api" )

@app.route("/")
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')