from utils.validadores import verificar_input_entero
from utils.decoradores import despedida

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
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            despedida()
            break

