from utils import decoradores
import time
from utils.generadores import generar_contenedor_random

def eliminar_contenedor(puerto):
    if not puerto.contenedores:
        print("⚠ No hay contenedores para eliminar.")
        time.sleep(1)
        return

    try:
        indice = int(input("Ingrese el número del contenedor a eliminar: "))

        if 1 <= indice <= len(puerto.contenedores):
            eliminado = puerto.contenedores.pop(indice - 1)
            print(f"🗑 Contenedor {eliminado.id} eliminado.")
        else:
            print("❌ Índice fuera de rango.")

    except ValueError:
        print("❌ Ingrese un número válido.")

    time.sleep(1)


def menu_ver_contenedores(puerto):
    while True:
        decoradores.cambio_de_pagina()
        decoradores.titulo_menu(f"CONTENEDORES EN {puerto.nombre.upper()}")
        
        if not puerto.contenedores:
            print("⚠ Este puerto no tiene contenedores registrados.")
        else:
            print(f"{'No.':<5} {'ID':<10} {'Tipo':<15} {'Peso Max':<10}")
            print("-" * 45)
            for i, contenedor in enumerate(puerto.contenedores, start=1):
                print(f"{i:<5} {contenedor.id:<10} {contenedor.tipo:<15} {contenedor.peso_maximo:<10}")
                time.sleep(0.1)
        
        print("-" * 30)
        print(" 1. Agregar contenedor")
        print(" 2. Eliminar contenedor")
        print(" 0. Volver")
        print("-" * 30)

        opcion = input("\nSeleccione una opción: ")

        if opcion == "0":
            return

        if opcion == "1":
            nuevo = generar_contenedor_random()
            puerto.contenedores.append(nuevo)
            print(f"\n✅ Contenedor {nuevo.id} agregado exitosamente.")
            time.sleep(1)

        elif opcion == "2":
            eliminar_contenedor(puerto)

        else:
            print("❌ Opción inválida.")
            time.sleep(1)


def menu_ver_puertos(puertos):
    while True:
        decoradores.cambio_de_pagina()
        decoradores.titulo_menu("LISTA DE PUERTOS")

        print(f"{'No.':<5} {'Nombre':<25} {'Ubicación':<15}")
        print("-" * 45)
        for i, puerto in enumerate(puertos, start=1):
            time.sleep(0.1)
            print(f"{i:<5} {puerto.nombre:<25} {puerto.ubicacion:<15}")
        
        print("\n 0. Volver al menú principal")
        print("-" * 30)

        try:
            time.sleep(1)
            opcion = int(input("\nSeleccione un puerto: "))

            if opcion == 0:
                return

            if 1 <= opcion <= len(puertos):
                puerto_seleccionado = puertos[opcion - 1]
                menu_ver_contenedores(puerto_seleccionado)
            else:
                print("Opción inválida.")

        except ValueError:
            print("Ingrese un número válido.")
