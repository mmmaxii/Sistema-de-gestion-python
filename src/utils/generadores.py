import random
from clases.contenedor import Contenedor
from clases.productos import Alimento, Tecnologia, Vehiculo
from modulos.config import (
    BASE_DATOS_ALIMENTOS, 
    BASE_DATOS_TECNOLOGIA, 
    BASE_DATOS_VEHICULOS,
    BASE_DATOS_CONTENEDORES
)



def generar_alimento_random():
    """Selecciona un alimento al azar de la base de datos y retorna la instancia."""
    # 1. Elegimos un nombre al azar de las llaves del diccionario
    nombre = random.choice(list(BASE_DATOS_ALIMENTOS.keys()))
    
    # 2. Obtenemos la tupla de datos: (peso, precio, requiere_frio)
    datos = BASE_DATOS_ALIMENTOS[nombre]
    
    # 3. Retornamos la instancia de la clase
    return Alimento(
        nombre=nombre, 
        peso=datos[0], 
        precio=datos[1], 
        requiere_frio=datos[2]
    )

def generar_tecnologia_random():
    """Selecciona un producto tecnológico al azar."""
    nombre = random.choice(list(BASE_DATOS_TECNOLOGIA.keys()))
    
    # datos: (peso, precio, marca)
    datos = BASE_DATOS_TECNOLOGIA[nombre]
    
    return Tecnologia(
        nombre=nombre, 
        peso=datos[0], 
        precio=datos[1], 
        marca=datos[2]
    )

def generar_vehiculo_random():
    """Selecciona un vehículo al azar."""
    nombre = random.choice(list(BASE_DATOS_VEHICULOS.keys()))
    
    # datos: (peso, precio, marca, anio)
    datos = BASE_DATOS_VEHICULOS[nombre]
    
    return Vehiculo(
        nombre=nombre, 
        peso=datos[0], 
        precio=datos[1], 
        marca=datos[2], 
        año=datos[3] 
    )

def generar_producto_general():
    """
    Función maestra: Lanza una moneda al aire y decide qué tipo de producto crear.
    Útil para llenar un contenedor mixto rápidamente.
    """
    categoria = random.choice(['alimento', 'tecnologia', 'vehiculo'])
    
    if categoria == 'alimento':
        return generar_alimento_random()
    elif categoria == 'tecnologia':
        return generar_tecnologia_random()
    else:
        return generar_vehiculo_random()






def generar_contenedor_random():
    """
    Selecciona un contenedor al azar de la base de datos estática (BASE_DATOS_CONTENEDORES).
    Retorna una instancia de la clase Contenedor.
    """
    # 1. Obtenemos todas las llaves (IDs) en una lista y elegimos una al azar
    lista_ids = list(BASE_DATOS_CONTENEDORES.keys())
    id_seleccionado = random.choice(lista_ids)
    
    # 2. Obtenemos el tipo asociado a ese ID
    tipo_seleccionado = BASE_DATOS_CONTENEDORES[id_seleccionado]
    
    # 3. Retornamos la instancia
    return Contenedor(id_contenedor=id_seleccionado, tipo_contenedor=tipo_seleccionado)



def eliminar_producto_random(contenedor):
    """
    Elimina un producto al azar del inventario (carga) del contenedor.
    """
    if not contenedor.carga:
        print("⚠ No hay productos para eliminar.")
        return

    # Seleccionamos una llave (nombre de producto) al azar
    nombre = random.choice(list(contenedor.carga.keys()))
    
    # Reducimos la cantidad en el inventario
    contenedor.carga[nombre] -= 1
    
    # Si la cantidad llega a 0, eliminamos la entrada del diccionario
    if contenedor.carga[nombre] <= 0:
        del contenedor.carga[nombre]
    
    print(f"🗑 Producto {nombre} eliminado.")