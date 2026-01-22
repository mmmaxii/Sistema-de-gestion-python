
class Contenedor:
    def __init__(self, id_contenedor, tipo_contenedor):
        self.id = id_contenedor
        self.tipo = tipo_contenedor  # Refrigerado, Seco, OpenTop
        self.carga = []  

    def agregar_producto(self, producto):

        if isinstance(producto, Alimento):
            if producto.requiere_frio and self.tipo != "Refrigerado":
                print(f"ERROR: ¡El alimento {producto.nombre} se va a podrir! Necesita contenedor Refrigerado.")
                return False
        
        self.carga.append(producto)
        print(f"Producto {producto.nombre} agregado con éxito.")
        return True