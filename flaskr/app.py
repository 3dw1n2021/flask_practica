from flaskr import create_app
from .modelos import db, Cancion, Usuario, Album, Medio

app = create_app('default')
app_context = app.app_context()
app_context.push()

# importamos la base de datos -# 3
db.init_app(app)
db.create_all()

# PRUEBA
with app.app_context():
    u = Usuario(nombre = "Juan", contrasena = "12345")
    a = Album(titulo = "prueba", anio =2000, descripcion = "texto", medio = Medio.CD )
    u.albumes.append(a)
    db.session.add(u)
    db.session.commit()
    print(Usuario.query.all())
    print(Usuario.query.all()[0].albumes)
    db.session.delete(u)
    print(Usuario.query.all())
    print(Album.query.all())
