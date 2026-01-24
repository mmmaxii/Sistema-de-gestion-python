# Validadores de datos para el menu principal. Inputs y demas.
import time
from modulos.config import PAISES_COSTEROS

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
    

def verificar_pais_costeros(pais):
    
    if pais not in PAISES_COSTEROS:
        return False
    return True