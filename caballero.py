from personaje import Personaje
from habilidad import Habilidad

class Caballero(Personaje):
    def ataque(self, target:Personaje):
        danio = self.__fuerza * 1.5
        target.__vida -= danio
        print(f"{self.__nombre} ataca a {target.__nombre} causando {danio} daño.")

    def usar_habilidad(self, habilidad:Habilidad, objetivo:Personaje):
        habilidad.casteo(self, objetivo)

    def __str__(self) -> str:
        return f'{self.__nombre}'