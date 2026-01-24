from utils.generadores import generar_producto_general

def menu_contenedores(puerto):
    while True:
        decoradores.cambio_de_pagina()
        print(f"\n--- CONTENEDORES EN {puerto.nombre} ---\n")

        for i, cont in enumerate(puerto.contenedores, start=1):
            print(f"{i}. {cont}")

        print("\n0. Volver")

        try:
            opcion = int(input("\nSeleccione un contenedor: "))

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
    while True:
        decoradores.cambio_de_pagina()
        print(f"\n--- CONTENEDOR {contenedor.id} ---")
        print(f"Tipo: {contenedor.tipo}")
        print(f"Carga actual: {len(contenedor.carga)} productos\n")

        if contenedor.carga:
            print("📦 Productos:")
            for prod in contenedor.carga:
                print(f" - {prod}")
        else:
            print("⚠ Contenedor vacío.")

        print("\n1. Agregar productos aleatorios")
        print("0. Volver")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "0":
            return

        if opcion == "1":
            agregar_productos_aleatorios(contenedor)


def agregar_productos_aleatorios(contenedor):
    try:
        cantidad = int(input("¿Cuántos productos desea agregar?: "))

        if cantidad <= 0:
            print("❌ La cantidad debe ser mayor a 0.")
            input("ENTER para continuar...")
            return

    except ValueError:
        print("❌ Ingrese un número válido.")
        input("ENTER para continuar...")
        return

    agregados = 0

    for _ in range(cantidad):
        producto = generar_producto_general()

        if contenedor.agregar_producto(producto):
            agregados += 1
        else:
            print("⚠ No se pudo agregar más productos.")
            break

    print(f"\n✅ Productos agregados: {agregados}/{cantidad}")
    input("ENTER para continuar...")
