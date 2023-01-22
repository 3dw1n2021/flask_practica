from flask import request
from ..modelos import db, Cancion, CancionSchema, Usuario, UsuarioSchema, Album, AlbumSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

cancion_schema = CancionSchema()
usuario_schema = UsuarioSchema()
album_schema = AlbumSchema()

class VistaCanciones(Resource):

    def post(self):
        nueva_cancion = Cancion(titulo = request.json['titulo'], 
                                minutos = request.json["minutos"],
                                segundos = request.json['segundos'],
                                interprete = request.json['interprete'])
        db.session.add(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)

    def get(self):
        return [cancion_schema.dump(ca) for ca in Cancion.query.all()]

class VistaCancion(Resource):
    
    def get(self, id_cancion):
        return cancion_schema.dump(Cancion.query.get_or_404(id_cancion))

    def put(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        cancion.titulo = request.json.get("titulo",cancion.titulo)
        cancion.minutos = request.json.get("minutos",cancion.minutos)
        cancion.segundos = request.json.get("segundos",cancion.segundos)
        cancion.interprete = request.json.get("interprete",cancion.interprete)
        db.session.commit()
        return cancion_schema.dump(cancion)

    def delete(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        db.session.delete(cancion)
        db.session.commit()
        return '', 204

class VistaSignIn(Resource):

    def post(self):
        nuevo_usuario = Usuario(nombre = request.json["nombre"], 
                                contrasena = request.json["contrasena"])
        db.session.add(nuevo_usuario)
        db.session.commit()
        return usuario_schema.dump(nuevo_usuario)

    def put(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        usuario.contrasena = request.json.get("contrasena",usuario.contrasena)
        db.session.commit()
        return usuario_schema.dump(usuario)

    def delete(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        db.session.delete(usuario)
        db.session.commit()
        return '', 204

class VistaAlbumsUsuario(Resource):

    def post(self, id_usuario):
        nuevo_album = Album(titulo=request.json["titulo"],
                             anio=request.json["anio"], 
                             descripcion=request.json["descripcion"], 
                             medio=request.json["medio"])
        usuario = Usuario.query.get_or_404(id_usuario)
        usuario.albumes.append(nuevo_album)

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return 'El usuario ya tiene un album con dicho nombre',409

        return album_schema.dump(nuevo_album)

    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return [album_schema.dump(al) for al in usuario.albumes]

