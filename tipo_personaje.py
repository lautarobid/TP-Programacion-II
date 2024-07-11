from habilidad import Habilidad
class TipoPersonaje:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__habilidades = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre: str) -> None:
        self.__nombre = new_nombre

    @property
    def habilidades(self) -> list:
        return self.__habilidades

    def añadir_habilidad(self, habilidad: Habilidad) -> str:
        self.__habilidades.append(habilidad)
        return f'Habilidad {habilidad.nombre} fue añadida a {self.__nombre}'