from flask import Flask, request, jsonify, redirect, render_template
from Config.db import app
from api.Cliente.apiclientes import ruta_cliente
from api.Prestamista.apiprestamistas import ruta_Prestamista
from api.Prestamo.apiprestamos import ruta_prestamo
from api.Detalle_Prestamo.apidetalle_prestamo import ruta_Detalle_Prestamo

app.register_blueprint(ruta_cliente, url_prefix = "/api" )
app.register_blueprint(ruta_Prestamista, url_prefix = "/api" )
app.register_blueprint(ruta_prestamo, url_prefix = "/api" )
app.register_blueprint(ruta_Detalle_Prestamo, url_prefix = "/api" )

@app.route("/")
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')