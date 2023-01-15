from flaskr import create_app
from .modelos import db, Cancion, Usuario, Album

app = create_app('default')
app_context = app.app_context()
app_context.push()

# importamos la base de datos -# 3
db.init_app(app)
db.create_all()
