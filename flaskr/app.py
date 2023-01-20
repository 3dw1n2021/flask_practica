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
    a = Album(titulo = "prueba", anio =2000, descripcion = "texto", medio = Medio.CD)
    c = Cancion(titulo = "mi canción", minutos = 1, segundos = 30, interprete = "Juanito")
    u.albumes.append(a)
    a.canciones.append(c)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    print(Album.query.all())
    print(Album.query.all()[0].canciones)
    print(Cancion.query.all())
    db.session.delete(a)
    print(Album.query.all())
    print(Cancion.query.all())
    
