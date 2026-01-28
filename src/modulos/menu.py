from time import time
from utils.validadores import verificar_input_entero, verificar_pais_costeros
import utils.decoradores as decoradores
import time
from clases.puertos import Puerto
from utils.generadores import generar_producto_general
from clases.contenedor import Contenedor
from clases.productos import Alimento, Tecnologia, Vehiculo
from .menu_puertos import menu_ver_puertos
from .menu_contenedor import menu_contenedores

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
            # Luego me metere en la logica de agregar puertos
            decoradores.cambio_de_pagina()
            decoradores.titulo_menu("AGREGAR PUERTO")
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

            decoradores.titulo_menu("ELIMINAR PUERTO")
            paises_disponibles = sorted({p.ubicacion for p in puertos_en_curso})
            print(f"Países con puertos registrados: {', '.join(paises_disponibles)}")
            ubicacion_buscada = input("Ingrese la ubicación para filtrar puertos: ")
            puertos_en_ubicacion = [p for p in puertos_en_curso if p.ubicacion.lower() == ubicacion_buscada.lower()]

            if not puertos_en_ubicacion:
                print(f"\nNo hay puertos registrados en la ubicación: {ubicacion_buscada}.")
                time.sleep(1)
            else:
                print(f"\nPuertos encontrados en {ubicacion_buscada}:")
                for p in puertos_en_ubicacion:
                    print(f"- {p.nombre}")
                    time.sleep(0.2)
                
                nombre_a_eliminar = input("\nIngrese el nombre del puerto que desea eliminar: ")
                puerto_a_borrar = next((p for p in puertos_en_ubicacion if p.nombre.lower() == nombre_a_eliminar.lower()), None)

                if puerto_a_borrar:
                    puertos_en_curso.remove(puerto_a_borrar)
                    print(f"\nEl puerto '{puerto_a_borrar.nombre}' ha sido eliminado exitosamente.")
                else:
                    print(f"\nNo se encontró ningún puerto con el nombre '{nombre_a_eliminar}' en esa ubicación.")
                
                input("\nPresione ENTER para volver al menú...")
                pass

        elif opcion == 0:
            
            decoradores.despedida_programa()
            return puertos_en_curso
            



