# Clase padre
class Producto:
    def __init__(self, nombre, peso, precio):
        self.nombre = nombre
        self.peso = peso
        self.precio = precio

class Alimento(Producto):
    def __init__(self, nombre, peso, precio, requiere_frio):
        super().__init__(nombre, peso, precio) 
        self.requiere_frio = requiere_frio
    
    def __str__(self):
        return f"{self.nombre} - {self.peso} kg - ${self.precio} - Requiere frío: {self.requiere_frio}"    

class Tecnologia(Producto):
    def __init__(self, nombre, peso, precio, marca):
        super().__init__(nombre, peso, precio)
        self.marca = marca

    def __str__(self):
        return f"{self.nombre} - {self.peso} kg - ${self.precio} - {self.marca}"

class ArticulosDomestico(Producto):
    def __init__(self, nombre, peso, precio, marca):
        super().__init__(nombre, peso, precio)
        self.marca = marca

    def __str__(self):
        return f"{self.nombre} - {self.peso} kg - ${self.precio} - {self.marca}"


class Vehiculo(Producto):
    def __init__(self, nombre, peso, precio, marca, año):
        super().__init__(nombre, peso, precio)
        self.marca = marca
        self.año = año
        
    def __str__(self):
        return f"{self.nombre} - {self.peso} kg - ${self.precio} - {self.marca} - {self.año}"



