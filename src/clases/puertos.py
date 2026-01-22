from .contenedor import Contenedor 

puertos_registrados = [
    Puerto("Puerto de San Antonio", "Chile", 10),
    Puerto("Puerto de Valparaíso", "Chile", 7),
    Puerto("Puerto de Róterdam", "Holanda", 15)
]

class Puerto:
    def __init__(self, nombre, ubicacion, capacidad_maxima):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.contenedores = [] 
        self.capacidad_maxima = capacidad_maxima 
        
    def __str__(self):
        return f"⚓ {self.nombre} ({self.ubicacion}) - Ocupación: {len(self.contenedores)}/{self.capacidad_maxima}"
    
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



def