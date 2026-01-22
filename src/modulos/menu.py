from utils.validadores import verificar_input_entero
import utils.decoradores as decoradores
import time
from clases.puertos import puertos_registrados



def menu_principal():
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
            # Recorremos la lista que importamos

            if not puertos_registrados:
                print("No hay puertos registrados.")
            else:
                for puerto in puertos_registrados:
                    print(puerto) # Esto usa el método __str__ que creamos
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
            break

