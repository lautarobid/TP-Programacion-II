class Mision:
    def __init__(self, nombre: str, descripcion: str, recompensa: str, mision_completa: bool = False):
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
    def descripcion(self, new_descripcion: str) -> None:
        self.__descripcion = new_descripcion

    @property
    def recompensa(self) -> str:
        return self.__recompensa

    @recompensa.setter
    def recompensa(self, new_recompensa: str) -> None:
        self.__recompensa = new_recompensa

    def mision_completada(self) -> str:
        self.__mision_completa = True
        return f"La misión '{self.__nombre}' ha sido completada."

    def esta_completada(self) -> bool:
        return self.__mision_completa

    def __str__(self) -> str:
        return (f"Misión: {self.__nombre}\n"
                f"Descripción: {self.__descripcion}\n"
                f"Recompensa: {self.__recompensa}\n"
                f"Completada: {'Sí' if self.__mision_completa else 'No'}")