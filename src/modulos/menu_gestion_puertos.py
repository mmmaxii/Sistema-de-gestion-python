import time
from utils import decoradores
from modulos.config import PAISES_COSTEROS
from utils.validadores import verificar_input_entero, verificar_pais_costeros
from clases.puertos import Puerto

def menu_eliminar_puerto(puertos):
    while True:
        decoradores.cambio_de_pagina()
        decoradores.titulo_menu("ELIMINAR PUERTO")

        if not puertos:
            print("⚠ No hay puertos registrados para eliminar.")
            time.sleep(1)
            return

        print(f"{'No.':<5} {'Nombre':<20} {'Ubicación':<15} {'Contenedores':<15}")
        print("-" * 60)
        for i, puerto in enumerate(puertos, start=1):
            info_contenedores = f"{len(puerto.contenedores)}/{puerto.capacidad_maxima}"
            print(f"{i:<5} {puerto.nombre:<20} {puerto.ubicacion:<15} {info_contenedores:<15}")
            time.sleep(0.1)
        
        print("-" * 60)
        print(" 0. Volver")
        print("-" * 30)

        try:
            opcion = int(input("\nIngrese el número del puerto a eliminar: "))

            if opcion == 0:
                return

            if 1 <= opcion <= len(puertos):
                puerto_a_eliminar = puertos[opcion - 1]
                
                print(f"\n¿Seguro que quieres eliminar el puerto: {puerto_a_eliminar.nombre}, ubicado en {puerto_a_eliminar.ubicacion}?")
                confirmacion = input("Escribe 'si' para confirmar: ").lower()

                if confirmacion == 'si':
                    puertos.pop(opcion - 1)
                    print(f"\n✅ El puerto '{puerto_a_eliminar.nombre}' ha sido eliminado exitosamente.")
                else:
                    print("\n❌ Operación cancelada.")
                
                time.sleep(1.5)
            else:
                print("❌ Opción inválida.")
                time.sleep(1)

        except ValueError:
            print("❌ Ingrese un número válido.")
            time.sleep(1)


def menu_agregar_puerto(puertos):
    while True:
        decoradores.cambio_de_pagina()
        decoradores.titulo_menu("AGREGAR PUERTO")
        
        nombre = input("Ingrese el nombre del puerto: ")
        
        print("\nPara ver la lista de países costeros válidos, escribe 'AYUDA'.")
        ubicacion = input("Ingrese la ubicación del puerto: ")

        if ubicacion.upper() == "AYUDA":
            print("\n--- LISTA DE PAÍSES COSTEROS VÁLIDOS ---")
            paises_ordenados = sorted(list(PAISES_COSTEROS))
            
            # Mostrar en columnas para ahorrar espacio
            col_width = 25
            for i in range(0, len(paises_ordenados), 3):
                row = paises_ordenados[i:i+3]
                
                # Imprime los países alineados en columnas (ljust rellena con espacios a la derecha)
                for pais in row:
                    print(pais.ljust(col_width), end="")
                print()
            
            print("-" * 60)
            input("\nPresione ENTER para continuar e ingresar la ubicación...")
            continue

        # Finalmente no utilice la funcion verificar_pais_costeros, pero la deje por si acaso.
        # La logica de verificacion esta en la clase puerto.
        if verificar_pais_costeros(ubicacion):
            capacidad_maxima = verificar_input_entero(input("Ingrese la capacidad máxima del puerto (1-100): "), rango=range(1, 101))
            
            if capacidad_maxima:
                puerto = Puerto(nombre, ubicacion, capacidad_maxima)
                puertos.append(puerto)
                print(f"\n✅ Puerto '{nombre}' en {ubicacion} agregado exitosamente.")
                time.sleep(1.5)
                return
        else:
            print("\n❌ El país no es costero o está mal escrito. Intente nuevamente.")
            time.sleep(1.5)

