from celery import Celery

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task() # 2: Decorador que hace esta función pase através de la cola
def registrar_log(usuario, fecha):
    with open('log_signin.txt', 'a+') as file: # 1: añadir lineas; +: para añadir si no existe
        file.write('{} - Inicio de sesion:{}\n'.format(usuario, fecha))