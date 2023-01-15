from flaskr import create_app
from .modelos import db, Cancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

# importamos la base de datos -# 3
db.init_app(app)
db.create_all()


#  PRUEBA
with app.app_context():
    c = Cancion(titulo = "Prueba", minutos = 2, segundos =25, interprete = "Juan Carlos" )
    c2 = Cancion(titulo = "Excelente", minutos = 2, segundos =25, interprete = "Edwin Torres" )
    db.session.add(c)
    db.session.add(c2)
    db.session.commit()
    print(Cancion.query.all())