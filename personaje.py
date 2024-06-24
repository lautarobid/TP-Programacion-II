from abc import ABC, abstractmethod
from typing import List
from item import Item
from skill import Skill

class Personaje(ABC):

    __nombres_registrados = set()

    def __init__(self, nombre: str, nivel: int, health: int, mana: int, fuerza: int, agilidad: int, vitalidad: int, energia: int, experience: int):
        self.__nombre = Personaje.__validar_nombre(nombre)
        self.nivel = nivel
        self.health = health
        self.mana = mana
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.vitalidad = vitalidad
        self.energia = energia
        self.experience = experience
        self.equipment: List[Item] = []

    @property 
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre:str):
        self.__nombre = new_nombre

    # @abstractmethod
    # def attack(self, target: 'Personaje'):
    #     print('ataque')

    # @abstractmethod
    # def use_skill(self, skill:Skill, target: 'Personaje'):
    #     print('usa skill')

    def subir_nivel(self):
        self.nivel += 1
        self.health += 10
        self.mana += 5
        self.fuerza += 2
        self.agilidad += 2
        self.vitalidad += 3
        self.energia += 2
        print(f"{self.nombre} subio de nivel a: {self.nivel}!")

    def equipar_item(self, item: Item):
        self.equipment.append(item)
        print(f"{self.nombre} equipado {item.nombre}.")

    def desequipar_item(self, item: Item):
        if item in self.equipment:
            self.equipment.remove(item)
            print(f"{self.nombre} desequipado {item.nombre}.")

    @classmethod
    def __validar_nombre(cls, nombre:str):
        if nombre in cls.__nombres_registrados:
            raise RuntimeError('ERROR- NOMBRE REGISTRADO')
        cls.__nombres_registrados.add(nombre)
        return nombre


class Wizard(Personaje):
    def attack(self, target:Personaje):
        danio = self.energia * 2
        target.health -= danio
        print(f"{self.nombre} ataca a {target.nombre} causando {danio} daño.")

    def use_skill(self, skill:Skill, target:Personaje):
        skill.cast(self, target)

class Knight(Personaje):
    def attack(self, target:Personaje):
        danio = self.fuerza * 1.5
        target.health -= danio
        print(f"{self.nombre} ataca a {target.nombre} causando {danio} daño.")

    def use_skill(self, skill:Skill, target:Personaje):
        skill.cast(self, target)