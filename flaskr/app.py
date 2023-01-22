from flaskr import create_app
from flask_restful import Api
from .modelos import db, Cancion, Usuario, Album, enum, CancionSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()

# importamos la base de datos -# 3
db.init_app(app)
db.create_all()

# Importamos el Api
api= Api(app)
