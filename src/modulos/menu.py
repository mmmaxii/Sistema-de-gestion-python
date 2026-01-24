from utils.validadores import verificar_input_entero, verificar_pais_costeros
import utils.decoradores as decoradores
import time
from clases.puertos import Puerto
from utils.generadores import generar_producto_general
from clases.contenedor import Contenedor
from clases.productos import Alimento, Tecnologia, Vehiculo

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
            print("\n--- AGREGAR PUERTO ---")
            nombre = input("Ingrese el nombre del puerto: ")
            ubicacion = input("Ingrese la ubicacion del puerto: ")

            if verificar_pais_costeros(ubicacion):
                capacidad_maxima = verificar_input_entero(input("Ingrese la capacidad maxima del puerto: "), rango = range(1,100))
                puerto = Puerto(nombre, ubicacion, capacidad_maxima)
                puertos_en_curso.append(puerto)
                input("\nPresione ENTER para volver al menú...")
                pass
            else:
                print("\nEl pais no es costero o está mal escrito.")

                time.sleep(1)
                input("\nPresione ENTER para volver al menú...")
                pass

        elif opcion == 3:
            # Luego me metere en la logica de eliminar puertos
            decoradores.cambio_de_pagina()
            print("\n--- ELIMINAR PUERTO ---")
            print("\nLista de puertos:")

            for puerto in puertos_en_curso:
                print(puerto)
                time.sleep(0.3)

            ubicacion_a_eliminar = input("Ingrese la ubicacion del puerto: ")

            for puerto_a_eliminar in puertos_en_curso:
                if puerto_a_eliminar.ubicacion == ubicacion_a_eliminar:
                    puertos_en_curso.remove(puerto_a_eliminar)
                    print(f"\nPuerto {puerto_a_eliminar.nombre} eliminado exitosamente.")
                    time.sleep(0.5)
                    input("\nPresione ENTER para volver al menú...")
                    break
                else:
                    print("\nNo existen puertos en esta ubicación.")
                    time.sleep(1)
                    input("\nPresione ENTER para volver al menú...")
                    break

        elif opcion == 4:
            
            decoradores.despedida_programa()
            return puertos_en_curso
            

