from personaje import Personaje
from habilidad import Habilidad

class Caballero(Personaje):
    def ataque(self, target: Personaje) -> str:
        danio = self.fuerza * 1.5
        target.vida -= danio
        return f"{self.nombre} ataca a {target.nombre} causando {danio} daño."

    def usar_habilidad(self, habilidad: Habilidad, objetivo: Personaje) -> str:
        return habilidad.casteo(self, objetivo)

    def __str__(self) -> str:
        return f'{self.nombre}'
    
    """
class Caballero(Personaje):
    def __init__(self, nombre, nivel, vida, mana, fuerza, agilidad, vitalidad, energia, experiencia):
        super().__init__(nombre, nivel, vida, mana, fuerza, agilidad, vitalidad, energia, experiencia)
        """