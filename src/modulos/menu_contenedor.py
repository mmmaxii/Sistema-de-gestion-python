from utils import decoradores
from utils.generadores import eliminar_producto_random
from utils.generadores import agregar_productos_aleatorios

def menu_contenedores(puerto):
    """
    Muestra los contenedores del puerto, gestiona errores de indice fuera de rango 
    y de valor no valido
    """
    while True:
        decoradores.cambio_de_pagina()
        decoradores.titulo_menu(f"CONTENEDORES EN {puerto.nombre.upper()}")

        print(f"{'No.':<5} {'Descripción':<30}")
        print("-" * 45)
        for i, cont in enumerate(puerto.contenedores, start=1):
            print(f"{i:<5} {str(cont):<30}")

        print("-" * 30)
        print(" 0. Volver")
        print("-" * 30)

        try:
            opcion = int(input("\nSeleccione un contenedor para ver detalles: "))

            if opcion == 0:
                return

            if 1 <= opcion <= len(puerto.contenedores):
                contenedor = puerto.contenedores[opcion - 1]
                menu_contenedor_individual(contenedor)
            else:
                print("❌ Opción inválida.")

        except ValueError:
            print("❌ Ingrese un número válido.")
            input("ENTER para continuar...")



def menu_contenedor_individual(contenedor):
    """
    Muestra los productos del contenedor, gestiona errores de indice fuera de rango 
    y de valor no valido
    """
    while True:
        decoradores.cambio_de_pagina()
        decoradores.titulo_menu(f"CONTENEDOR {contenedor.id}")
        
        print(f" Tipo: {contenedor.tipo}")
        print(f" Carga actual: {contenedor.calcular_cantidad_productos()} productos")
        print("-" * 30)

        
        if contenedor.carga:
            print(" 📦 Productos:")
            for item in contenedor.carga.values():
                producto = item["producto"]
                cantidad = item["cantidad"]
                print(f"  - {cantidad}x {producto}")
        else:
            print(" ⚠ Contenedor vacío.")

        print("-" * 30)
        print(" 1. Agregar productos aleatorios")
        print(" 2. Eliminar productos aleatorios")
        print(" 0. Volver")
        print("-" * 30)

        opcion = input("\nSeleccione una opción: ")

        if opcion == "0":
            return

        if opcion == "1":
            agregar_productos_aleatorios(contenedor)

        if opcion == "2":
            eliminar_producto_random(contenedor)


