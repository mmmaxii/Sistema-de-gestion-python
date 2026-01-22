# Incorporar cosas como medir tiempos de ejecucion, tambien algo que confirme la acción.
import time

def despedida_programa():
    """
    Decorador que se despide del usuario y espera 2 segundos antes de continuar.
    """
    print("Saliendo... ¡Hasta pronto!")
    time.sleep(1)
            

def cambio_de_pagina():
    """
    Solo printea que se cambia de pagina y espera dos segundos.
    """
    print("Cambiando de pagina...")
    time.sleep(1)