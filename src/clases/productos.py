# Clase padre
class Producto:
    def __init__(self, nombre: str, peso: int, precio: int):
        self.nombre = nombre
        self.peso = peso
        self.precio = precio
    
    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "nombre": self.nombre,
            "peso": self.peso,
            "precio": self.precio
        }



class Alimento(Producto):
    def __init__(self, nombre: str, peso: int, precio: int, requiere_frio:  bool):
        super().__init__(nombre, peso, precio) 
        self.requiere_frio = requiere_frio
    
    def __str__(self):
        if self.requiere_frio:
            return f"{self.nombre} - {self.peso} kg - ${self.precio} - Requiere frío"
        else:
            return f"{self.nombre} - {self.peso} kg - ${self.precio} - No requiere frío"
    
    def to_dict(self):
        data = super().to_dict()
        data["requiere_frio"] = self.requiere_frio
        return data 



class Tecnologia(Producto):
    def __init__(self, nombre: str, peso: int, precio: int, marca: str):
        super().__init__(nombre, peso, precio)
        self.marca = marca

    def __str__(self):
        return f"{self.nombre} - {self.peso} kg - ${self.precio} - {self.marca}"

    def to_dict(self):
        data = super().to_dict()
        data["marca"] = self.marca
        return data 



class Vehiculo(Producto):
    def __init__(self, nombre: str, peso: int, precio: int, marca: str, año: int):
        super().__init__(nombre, peso, precio)
        self.marca = marca
        self.año = año
        
    def __str__(self):
        return f"{self.nombre} - {self.peso} kg - ${self.precio} - {self.marca} - {self.año}"

    def to_dict(self):
        data = super().to_dict()
        data["marca"] = self.marca
        data["año"] = self.año
        return data 



