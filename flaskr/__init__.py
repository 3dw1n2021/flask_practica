from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    # Crear template de BBDD
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///practica.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # desactiva warnings
    return app
