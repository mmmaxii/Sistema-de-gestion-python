from .productos import Alimento, Tecnologia, Vehiculo

class Contenedor:
    def __init__(self, id_contenedor, tipo_contenedor):
        self.id = id_contenedor
        self.tipo = tipo_contenedor  # Refrigerado, Seco, OpenTop
        self.carga = []  
        self.peso_maximo = 29000 #kg

    
    def __str__(self):
        return f"{self.id} - {self.tipo} - {self.peso_actual}/{self.peso_maximo} kg"

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "peso_maximo": self.peso_maximo,
            "carga": [producto.to_dict() for producto in self.carga]
        }

    def agregar_producto(self, producto):

        if isinstance(producto, Alimento):
            if producto.requiere_frio and self.tipo != "Refrigerado":
                print(f"ERROR: ¡El alimento {producto.nombre} se va a podrir! Necesita contenedor Refrigerado.")
                return False
        
        if isinstance(producto, Vehiculo):
            if self.tipo != "OpenTop":
                print(f"ERROR: ¡El vehiculo {producto.nombre} se va a dañar! Necesita contenedor OpenTop.")
                return False
        
        if self.peso_actual + producto.peso > self.peso_maximo:
            print(f"ERROR: ¡El contenedor {self.id} está lleno! No cabe el producto {producto.nombre}.")
            return False

        self.carga.append(producto)
        print(f"Producto {producto.nombre} agregado con éxito.")
        return True