class Habilidad:
    def __init__(self, nombre: str, mana_costo: int, danio: int, enfriamiento: float):
        self.__nombre = nombre
        self.__mana_costo = mana_costo
        self.__danio = danio
        self.__enfriamiento = enfriamiento

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre: str) -> None:
        self.__nombre = new_nombre

    @property
    def mana_costo(self) -> int:
        return self.__mana_costo

    @mana_costo.setter
    def mana_costo(self, new_mana_costo: int) -> None:
        self.__mana_costo = new_mana_costo

    @property
    def danio(self) -> int:
        return self.__danio

    @danio.setter
    def danio(self, new_danio: int) -> None:
        self.__danio = new_danio

    @property
    def enfriamiento(self) -> float:
        return self.__enfriamiento

    @enfriamiento.setter
    def enfriamiento(self, new_enfriamiento: float) -> None:
        self.__enfriamiento = new_enfriamiento
        
    