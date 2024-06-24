from personaje import *
from abc import ABC, abstractmethod
from skill import Skill
from item import Item

class Monstruos():
    def __init__(self, nombre:str, tipo:str, vida:int, ataque:int, defensa:int, velocidad:int):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__vida = vida
        self.__ataque = ataque
        self.__defensa = defensa
        self.__velocidad = velocidad

    @property 
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre:str):
        self.__nombre = new_nombre
    
    @property 
    def tipo(self) -> str:
        return self.__tipo
    
    @tipo.setter
    def tipo(self, new_tipo:str):
        self.__tipo = new_tipo
    
    @property 
    def vida(self) -> int:
        return self.__vida
    
    @vida.setter
    def vida(self, new_vida:int):
        self.__vida = new_vida

    @property 
    def ataque(self) -> int:
        return self.__ataque
    
    @ataque.setter
    def ataque(self, new_ataque:int):
        self.__ataque = new_ataque
        
    @property 
    def defensa(self) -> int:
        return self.__defensa
    
    @defensa.setter
    def defensa(self, new_defensa:int):
        self.__defensa = new_defensa

    @property 
    def velocidad(self) -> int:
        return self.__velocidad
    
    @velocidad.setter
    def velocidad(self, new_velocidad:int):
        self.__velocidad = new_velocidad

    def atacar(self, Personaje:Personaje):
        Personaje.health -= self.ataque - Personaje.agilidad
        if Personaje.health < 0:
            Personaje.health = 0
        print(f"{self.nombre} ataco a {Personaje.nombre} por {self.ataque - Personaje.agilidad} de daño")
        print(f"La vida de {Personaje.nombre} es de {Personaje.health}")

    def recibir_ataque(self, Personaje:Personaje):
        self.vida -= Personaje.fuerza - self.defensa
        if self.vida < 0:
            self.vida = 0
        print(f"{Personaje.nombre} ataco a {self.nombre} por {Personaje.fuerza - self.defensa} de daño")
        print(f"La vida de {self.nombre} es de {self.vida}")
    
    def recibir_skill(self, Personaje:Personaje, skill:Skill):
        self.vida -= skill.danio - self.defensa
        if self.vida < 0:
            self.vida = 0
        print(f"{Personaje.nombre} uso {skill.nombre} a {self.nombre} por {skill.danio} de daño")
        print(f"La vida de {self.nombre} es de {self.vida}")
    
    def pelea(self, personaje:Personaje, skill:Skill):
        print(f"Pelear contra {self.nombre}...")
        print("----------------------------------------------")
        while self.vida >  0 and personaje.health > 0:
                self.recibir_skill(personaje, skill)
                if self.vida > 0:
                    self.atacar(personaje)
                print("----------------------------------------------")
        if self.vida <= 0:
            print(f"{self.nombre} ha sido derrotado.")
        else:
            print(f"{personaje.nombre} ha sido derrotado.")
        


    def __str__(self):
        return f"Nombre: {self.nombre} \nTipo: {self.tipo} \nVida: {self.vida} \nAtaque: {self.ataque} \nDefensa: {self.defensa} \nVelocidad: {self.velocidad}"
    
class Dragon(Monstruos):
    pass

class Orco(Monstruos):
    pass

class Arania(Monstruos):
    pass