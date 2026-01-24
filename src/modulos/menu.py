from utils.validadores import verificar_input_entero
import utils.decoradores as decoradores
import time
from clases.puertos import puertos_registrados


def menu_principal(puertos_en_curso):
    """Función que muestra el menú principal del sistema."""
    while True:
        print("Menu principal \n"
            + "1. Ver puertos \n"
            + "2. Agregar puerto \n"
            + "3. Eliminar puerto \n"
            + "4. Salir \n")

        opcion = verificar_input_entero(input("Ingrese una opcion: "), rango = range(1,5))

        if opcion == 1:
            decoradores.cambio_de_pagina()
            print("\n--- LISTA DE PUERTOS ACTUALES ---")
            # Recorremos la lista que importamos, luego sera una lista que leeremos con un 
            # Archivo JSON

            # Quiero mejor extraer la lista de puertos de un archivo JSON. Luego modifcarlos si es
            # Necesario y guardarlos nuevamente en el archivo JSON. 
            # Para esto haré una funcion que extraiga todo. Luego otra que guarde todo.

            
            for puerto in puertos_en_curso:
                print(puerto) # Esto usa el método __str__ que creamos en la clase.
                time.sleep(0.3)
                
            # Luego me metere en la logica de gestionar los contenedores y demas
            input("\nPresione ENTER para volver al menú...")
            pass

        elif opcion == 2:
            # Luego me metere en la logica de agregar puertos
            decoradores.cambio_de_pagina()

            pass

        elif opcion == 3:
            # Luego me metere en la logica de eliminar puertos
            decoradores.cambio_de_pagina()
            pass

        elif opcion == 4:
            
            decoradores.despedida_programa()
            return puertos_en_curso
            

