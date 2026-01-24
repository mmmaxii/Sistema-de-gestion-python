# Sistema de gestión de clientes
from modulos.menu import menu_principal
from repositorios.repositorios_puerto import RepositorioPuertos


if __name__ == "__main__":
    repositorio_puertos = RepositorioPuertos()
    puertos_cargados = repositorio_puertos.cargar()
    puertos_registrados = menu_principal(puertos_cargados)
    repositorio_puertos.guardar(puertos_registrados)
