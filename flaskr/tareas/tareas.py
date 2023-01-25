from celery import Celery

Celery_app = Celery(__name__, bloker='redis://localhost:6379/0')


def registrar_log(usuario, fecha):
    with open('log_singin.txt', 'a+') as file:   # a: añadir lineas; +: para añadir si no existe
        file.write('{} - inicio de sesion; {}\n'.format(usuario, fecha))