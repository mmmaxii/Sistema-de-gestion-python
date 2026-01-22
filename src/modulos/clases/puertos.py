from clases.contenedor import Contenedor

# Vamos a modificar luego esto.
class Puerto:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.contenedores = []

    def agregar_contenedor(self, contenedor: Contenedor):
        self.contenedores.append(contenedor)
        print(f"Contenedor {contenedor.id} agregado con éxito.")
        return True

    def eliminar_contenedor(self, contenedor: Contenedor):
        if contenedor in self.contenedores:
            self.contenedores.remove(contenedor)
            print(f"Contenedor {contenedor.id} eliminado con éxito.")
            return True
        else:
            print(f"Contenedor {contenedor.id} no encontrado.")
            return False

    def mostrar_contenedores(self):
        if self.contenedores:
            print("Contenedores:")
            for contenedor in self.contenedores:
                print(f"ID: {contenedor.id}, Tipo: {contenedor.tipo}")
        else:
            print("No hay contenedores en el puerto.")

