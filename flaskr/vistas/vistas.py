from flask import request
from ..modelos import db, Cancion, CancionSchema
from flask_restful import Resource

Cancion_schema = CancionSchema()

class VistaCanciones(Resource):

    def post(self):
        nueva_cancion = Cancion(titulo = request.json['titulo'], 
                                minutos = request.json["minutos"],
                                segundos = request.json['segundos'],
                                interprete = request.json['interprete'])
        db.session.add(nueva_cancion)
        db.session.commit()
        return Cancion_schema.dump(nueva_cancion)