from abc import ABC,abstractmethod
from tipopersonaje import TipoPersonaje
from item import Item

class Personaje(ABC):
    @abstractmethod
    def __init__(self, name: str, level: int, health: int, mana: int, strength: int, agility: int, vitality: int, energy: int, experience: int):
        self.name = name
        self.level = level
        self.health = health
        self.mana = mana
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.vitalidad = vitalidad
        self.energia = energia
        self.experience = experience
        self.equipment = []

@abstractmethod
