from flask import Flask, request, jsonify, redirect, render_template
from Config.db import app
from api.Cliente.apiclientes import ruta_cliente
from api.Prestamo.apiprestamos import ruta_prestamo
from api.Prestamistas.apiprestamistas import ruta_prestamistas
from api.Detalle_prestamos.detalle_prestamos import ruta_detalle_prestamo

app.register_blueprint(ruta_cliente, url_prefix = "/api" )
app.register_blueprint(ruta_prestamo, url_prefix = "/api" )
app.register_blueprint(ruta_prestamistas, url_prefix = "/api" )
app.register_blueprint(ruta_detalle_prestamo, url_prefix = "/api" )

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')