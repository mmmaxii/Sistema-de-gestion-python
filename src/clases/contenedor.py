from .productos import Alimento, Tecnologia, Vehiculo

class Contenedor:
    def __init__(self, id_contenedor, tipo_contenedor):
        self.id = id_contenedor
        self.tipo = tipo_contenedor  # Refrigerado, Seco, OpenTop
        self.carga = {}  # Diccionario: { nombre_producto: {"producto": obj_producto, "cantidad": int} }
        self.peso_maximo = 100000 #kg
        self.peso_actual = round(self.calcular_peso_actual(), 2)

    def calcular_peso_actual(self):
        total = 0
        # se recorre el diccionario de la carga y se suma el peso de cada producto
        for item in self.carga.values():
            total += item["producto"].peso * item["cantidad"]
        return total
    
    def calcular_cantidad_productos(self):
        total = 0                           
        for item in self.carga.values():
            total += item["cantidad"]
        return total

    def __str__(self):
        # Recalcular peso actual al mostrar para asegurar consistencia
        self.peso_actual = self.calcular_peso_actual()
        return f"📦 {self.id} - {self.tipo} - {self.peso_actual}/{self.peso_maximo} kg"

    def to_dict(self):
        """
        Convierte el contenedor a un diccionario para guardarlo en un archivo JSON.
        """
        lista_carga = []
        for item in self.carga.values():
            prod_dict = item["producto"].to_dict()
            prod_dict["cantidad"] = item["cantidad"] # Agregamos cantidad al dict del producto para guardar
            lista_carga.append(prod_dict)

        return {
            "id": self.id,
            "tipo": self.tipo,
            "peso_maximo": self.peso_maximo,
            "carga": lista_carga
        }

    def agregar_producto(self, producto):
        # Validaciones de Tipo
        if isinstance(producto, Alimento):
            if producto.requiere_frio and self.tipo != "Refrigerado":
                print(f"ERROR: ¡El alimento {producto.nombre} se va a podrir! Necesita contenedor Refrigerado.")
                return False
        
        if isinstance(producto, Vehiculo):
            if self.tipo != "OpenTop":
                print(f"ERROR: ¡El vehiculo {producto.nombre} se va a dañar! Necesita contenedor OpenTop.")
                return False
        
        # Validación de Peso
        if self.peso_actual + producto.peso > self.peso_maximo:
            print(f"ERROR: ¡El contenedor {self.id} está lleno! No cabe el producto {producto.nombre}.")
            return False

        # Agregar o Actualizar
        if producto.nombre in self.carga:
            self.carga[producto.nombre]["cantidad"] += 1
            print(f"Producto {producto.nombre} agregado (Cantidad: {self.carga[producto.nombre]['cantidad']}).")
        else:
            self.carga[producto.nombre] = {"producto": producto, "cantidad": 1}
            print(f"Producto {producto.nombre} agregado con éxito.")
        
        self.peso_actual += producto.peso
        return True