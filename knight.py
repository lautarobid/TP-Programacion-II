from personaje import Personaje
from skill import Skill

class Knight(Personaje):
    def attack(self, target:Personaje):
        danio = self.fuerza * 1.5
        target.health -= danio
        print(f"{self.nombre} ataca a {target.nombre} causando {danio} daño.")

    def use_skill(self, skill:Skill, target:Personaje):
        skill.cast(self, target)

    def __str__(self) -> str:
        return f'{self.nombre}'