from flaskr import create_app
from .modelos import db, Cancion, Usuario, Album, enum, CancionSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()

# importamos la base de datos -# 3
db.init_app(app)
db.create_all()

#PRUEBA 
with app.app_context():

    c = Cancion(titulo="Prueba", minutos=2, segundos=20, interprete="Sultanito")
    c_schema = CancionSchema()
    db.session.add(c)
    db.session.commit()
    print([c_schema.dump(c) for c in Cancion.query.all()])