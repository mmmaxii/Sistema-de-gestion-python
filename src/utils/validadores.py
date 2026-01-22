# Validadores de datos para el menu principal. Inputs y demas.
import time

def verificar_input_entero(input_usuario, rango):
    try:
        input_usuario = int(input_usuario)
        if input_usuario not in rango:
            print(f"Error: Debes ingresar un numero entero entre {rango[0]} y {rango[-1]}")
            time.sleep(1)
            return None
        return input_usuario
    except ValueError:
        print("Error: Debes ingresar un numero entero.")
        time.sleep(1)
        return None