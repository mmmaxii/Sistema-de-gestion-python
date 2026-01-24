from multiprocessing.sharedctypes import Value
from .contenedor import Contenedor 
from modulos.config import PAISES_COSTEROS


def quitar_tildes_y_mayus(string):
    string = string.lower()
    string = string.replace("á", "a")
    string = string.replace("é", "e")
    string = string.replace("í", "i")
    string = string.replace("ó", "o")
    string = string.replace("ú", "u")
    return string


class PaisNoCostero(ValueError):
    pass

class Puerto:
    def __init__(self, nombre, ubicacion, capacidad_maxima):
        self._validar_pais(ubicacion)
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.contenedores = [] 
        self.capacidad_maxima = capacidad_maxima 
        
    def __str__(self):
        return f"⚓ {self.nombre} ({self.ubicacion}) - Ocupación: {len(self.contenedores)}/{self.capacidad_maxima}"

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "ubicacion": self.ubicacion,
            "capacidad_maxima": self.capacidad_maxima,
            "contenedores": [c.to_dict() for c in self.contenedores]
        }
    
    # Con esta funcion verificamos si el pais ingresado es costero, en caso de que no, se lanza un error, PERO,
    # no para el programa.
    def _validar_pais(self, ubicacion):
        if quitar_tildes_y_mayus(ubicacion) not in PAISES_COSTEROS:
            raise PaisNoCostero(f"El pais {ubicacion} no es costero.")

    def agregar_contenedor(self, contenedor):
        """
        Agrega un contenedor solo si hay espacio disponible.
        Retorna True si se agregó, False si el puerto estaba lleno.
        """
        if len(self.contenedores) >= self.capacidad_maxima:
            print(f" ERROR: El {self.nombre} está lleno. No cabe el contenedor {contenedor.id}.")
            return False
        
        self.contenedores.append(contenedor)
        print(f" Contenedor {contenedor.id} ingresado exitosamente al {self.nombre}.")
        return True



puertos_registrados = [
    Puerto("Puerto de San Antonio", "Chile", 10),
    Puerto("Puerto de Valparaíso", "Chile", 7),
    Puerto("Puerto de Róterdam", "Holanda", 15)
]
