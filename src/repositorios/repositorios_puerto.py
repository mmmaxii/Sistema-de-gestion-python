import json
from pathlib import Path
from clases.puertos import Puerto
from clases.contenedor import Contenedor
import time 


from clases.productos import (
    Alimento,
    Tecnologia,
    Vehiculo
)

def _producto_from_dict(data):
    tipo = data["tipo"]

    if tipo == "Alimento":
        return Alimento(
            data["nombre"],
            data["peso"],
            data["precio"],
            data["requiere_frio"]
        )

    if tipo == "Tecnologia":
        return Tecnologia(
            data["nombre"],
            data["peso"],
            data["precio"],
            data["marca"]
        )

    if tipo == "ArticulosDomestico":
        return ArticulosDomestico(
            data["nombre"],
            data["peso"],
            data["precio"],
            data["marca"]
        )

    if tipo == "Vehiculo":
        return Vehiculo(
            data["nombre"],
            data["peso"],
            data["precio"],
            data["marca"],
            data["año"]
        )

    raise ValueError(f"Tipo de producto desconocido: {tipo}")


def _contenedor_from_dict(data):
    contenedor = Contenedor(
        data["id"],
        data["tipo"]
    )
    contenedor.peso_maximo = data["peso_maximo"]

    for prod_data in data["carga"]:
        producto = _producto_from_dict(prod_data)
        cantidad = prod_data.get("cantidad", 1)  # Default 1 para compatibilidad
        
        # Insertar directamente para evitar prints de agregar_producto
        contenedor.carga[producto.nombre] = {
            "producto": producto,
            "cantidad": cantidad
        }
    
    # Recalcular peso inicial
    contenedor.peso_actual = contenedor.calcular_peso_actual()

    return contenedor


def _puerto_from_dict(data):
    puerto = Puerto(
        data["nombre"],
        data["ubicacion"],
        data["capacidad_maxima"]
    )

    for cont_data in data["contenedores"]:
        puerto.contenedores.append(
            _contenedor_from_dict(cont_data)
        )

    return puerto

def security_check(ruta):
    puerto = Puerto("Puerto de San Antonio", "Chile", 1)
    contenedor = Contenedor("CONT-001", "OpenTop")

    contenedor.agregar_producto(Alimento("Salmon", 500, 3000, True))
    contenedor.agregar_producto(Tecnologia("Notebook", 2500, 800000, "Lenovo"))
    contenedor.agregar_producto(Vehiculo("Motocicleta", 180000, 2500000, "Yamaha", 2022))

    puerto.agregar_contenedor(contenedor)

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump([puerto.to_dict()], f, indent=4, ensure_ascii=False)

    return [puerto.to_dict()]

class RepositorioPuertos:

    def __init__(self, ruta=None):
        base_dir = Path(__file__).resolve().parent.parent
        self.ruta = ruta or base_dir / "data" / "puertos.json"
    
    def guardar(self, puertos):
        with open(self.ruta, "w", encoding="utf-8") as f:
            json.dump(
                [p.to_dict() for p in puertos],
                f,
                indent=4,
                ensure_ascii=False
            )


    def cargar(self):
        try:
            with open(self.ruta, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, list) or not data:
                raise ValueError("Estructura JSON inválida o vacía")
        
        except (FileNotFoundError, json.decoder.JSONDecodeError, ValueError):
            print("\n Inicializando archivo de puertos por defecto...\n")
            time.sleep(1)
            data = security_check(self.ruta)
  
        return [_puerto_from_dict(p) for p in data]


