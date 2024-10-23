from flask import Flask
from Aplicacion.entradas import main


def create_app():
    app = Flask(__name__)

    # Registrar el blueprint
    app.register_blueprint(main)

    return app