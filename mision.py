class Mision:
    def __init__(self, nombre: str, descripcion: str, recompensa:str, mision_completa:bool=False):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__recompensa = recompensa
        self.__mision_completa = mision_completa

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre: str) -> None:
        self.__nombre = new_nombre

    @property
    def descripcion(self) -> str:
        return self.__descripcion

    @descripcion.setter
    def description(self, new_descripcion: str) -> None:
        self.__descripcion = new_descripcion

    @property
    def recompensa(self) -> str:
        return self.__recompensa

    @recompensa.setter
    def rewards(self, new_recompensa: str) -> None:
        self.__recompensa = new_recompensa

    def mision_completada(self):
        self.__mision_completa = True

    def esta_completada(self) -> bool:
        return self.__mision_completa