from flask import Flask, request, jsonify, redirect, render_template
from ConfigJ.db import app
from apiJ.Cliente.apicliente import ruta_cliente
from apiJ.Prestamo.apiprestamo import ruta_prestamo

app.register_blueprint(ruta_cliente, url_prefix = "/api" )
app.register_blueprint(ruta_prestamo, url_prefix = "/api" )

@app.route("/")
def index():
    return "Hola Mundo Juan"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')