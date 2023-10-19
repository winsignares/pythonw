from flask import Flask, request, jsonify, redirect, render_template
from Config.db import app
from api.Cliente.apiclientes import ruta_cliente
from api.Prestamista.apiprestamista import ruta_prestamista
from api.Prestamo.apiprestamos import ruta_prestamo
from api.PrestamoDetalle.apiprestamodetalle import ruta_prestamodetalle

app.register_blueprint(ruta_cliente, url_prefix = "/api" )
app.register_blueprint(ruta_prestamista, url_prefix = "/api" )
app.register_blueprint(ruta_prestamo, url_prefix = "/api" )
app.register_blueprint(ruta_prestamodetalle, url_prefix = "/api" )

@app.route("/")
def index():
    return "HELLO"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')