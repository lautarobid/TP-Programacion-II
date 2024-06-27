from personaje import Personaje
from habilidad import Habilidad

class Mago(Personaje):
    def ataque(self, target:Personaje):
        danio = self.__energia * 2
        target.__vida -= danio
        print(f"{self.__nombre} ataca a {target.__nombre} causando {danio} daño.")

    def usar_habilidad(self, habilidad:Habilidad, objetivo:Personaje):
        habilidad.casteo(self, objetivo)
    
    def __str__(self) -> str:
        return f'{self.__nombre}'