# Incorporar cosas como medir tiempos de ejecucion, tambien algo que confirme la acción.
import time
import os

def despedida_programa():
    """
    Decorador que se despide del usuario y espera 2 segundos antes de continuar.
    """
    print("\n" + "="*30)
    print(f"{'¡HASTA PRONTO!':^30}")
    print("="*30 + "\n")
    time.sleep(1)
            

def cambio_de_pagina():
    """
    Simula un cambio de página limpiando la pantalla o separando con líneas.
    """
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')

def titulo_menu(texto):
    """
    Imprime un título de menú formateado.
    """
    print("=" * 30)
    print(f"{texto:^30}")
    print("=" * 30)