# Incorporar cosas como medir tiempos de ejecucion, tambien algo que confirme la acción.

import time
from functools import wraps

def despedida(func):
    """
    Decorador que se despide del usuario y espera 2 segundos antes de continuar.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Saliendo... ¡Hasta pronto!")
        time.sleep(2)
        return func(*args, **kwargs)
    return wrapper