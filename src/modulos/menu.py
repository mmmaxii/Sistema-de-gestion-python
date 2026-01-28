from time import time
from utils.validadores import verificar_input_entero, verificar_pais_costeros
import utils.decoradores as decoradores
import time
from clases.puertos import Puerto
from .menu_puertos import menu_ver_puertos
from .menu_gestion_puertos import menu_eliminar_puerto, menu_agregar_puerto


def menu_principal(puertos_en_curso):
    """Función que muestra el menú principal del sistema."""
    while True:
        decoradores.cambio_de_pagina()
        decoradores.titulo_menu("MENÚ PRINCIPAL")
        print(" 1. Ver puertos")
        print(" 2. Agregar puerto")
        print(" 3. Eliminar puerto")
        print(" 0. Salir")
        print("-" * 30)

        opcion = verificar_input_entero(input("Ingrese una opcion: "), rango = range(0,4))

        if opcion == 1:
            menu_ver_puertos(puertos_en_curso)

        elif opcion == 2:
            menu_agregar_puerto(puertos_en_curso)

        elif opcion == 3:
            menu_eliminar_puerto(puertos_en_curso)

        elif opcion == 0:
            
            decoradores.despedida_programa()
            return puertos_en_curso
            



