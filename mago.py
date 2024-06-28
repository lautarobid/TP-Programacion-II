from personaje import Personaje
from habilidad import Habilidad

class Mago(Personaje):
    def ataque(self, target: Personaje) -> str:
        danio = self.energia * 2
        target.vida -= danio
        return f"{self.nombre} ataca a {target.nombre} causando {danio} daño."

    def usar_habilidad(self, habilidad: Habilidad, objetivo: Personaje) -> str:
        return habilidad.casteo(self, objetivo)
    
    def __str__(self) -> str:
        return f'{self.nombre}'