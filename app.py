from flask import Flask, request, jsonify, redirect, render_template
from Config.db import app
from api.Cliente.apiclientes import ruta_cliente

app.register_blueprint(ruta_cliente, url_prefix = "/api" )


@app.route("/")
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')