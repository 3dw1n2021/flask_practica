from flaskr import create_app
from flask_restful import Api
from .modelos import db, Cancion, Usuario, Album, enum, CancionSchema
from .vistas import VistaCanciones, VistaCancion, VistaSignIn, VistaAlbumsUsuario, VistaAlbum

app = create_app('default')
app_context = app.app_context()
app_context.push()

# importamos la base de datos -# 3
db.init_app(app)
db.create_all()

# Importamos el Api
api= Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/cancion/<int:id_cancion>')
api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaAlbumsUsuario, '/usuario/<int:id_usuario>/albumes')
api.add_resource(VistaAlbum, '/album/<int:id_album>')