from personaje import *
from habilidad import Habilidad

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
        Personaje.__vida -= self.__ataque - Personaje.__agilidad
        if Personaje.__vida < 0:
            Personaje.__vida = 0
        print(f"{self.__nombre} ataco a {Personaje.__nombre} por {self.__ataque - Personaje.__agilidad} de daño")
        print(f"La vida de {Personaje.__nombre} es de {Personaje.__vida}")

    def recibir_ataque(self, personaje:Personaje):
        self.__vida -= personaje.__fuerza - self.__defensa
        if self.__vida < 0:
            self.__vida = 0
        print(f"{personaje.__nombre} ataco a {self.__nombre} por {personaje.__fuerza - self.__defensa} de daño")
        print(f"La vida de {self.__nombre} es de {self.__vida}")
    
    def recibir_habilidad(self, personaje:Personaje, habilidad:Habilidad):
        self.__vida -= habilidad.__danio - self.__defensa
        if self.__vida < 0:
            self.__vida = 0
        print(f"{personaje.__nombre} uso {habilidad.__nombre} a {self.__nombre} por {habilidad.__danio} de daño")
        print(f"La vida de {self.__nombre} es de {self.__vida}")
    
    def pelea(self, personaje:Personaje, habilidad:Habilidad):
        vida_inicial = self.__vida
        print(f"Pelear contra {self.__nombre}...")
        print("----------------------------------------------")
        while self.__vida >  0 and personaje.__vida > 0:
                self.recibir_habilidad(personaje, habilidad)
                if self.__vida > 0:
                    self.atacar(personaje)
                print("----------------------------------------------")
        if self.__vida <= 0:
            print(f"{self.__nombre} ha sido derrotado.")
            self.__vida = vida_inicial
        else:
            print(f"{personaje.__nombre} ha sido derrotado.")
        

    def __str__(self):
        return f"Nombre: {self.__nombre} \nTipo: {self.__tipo} \nVida: {self.__vida} \nAtaque: {self.__ataque} \nDefensa: {self.__defensa} \nVelocidad: {self.__velocidad}"
    
class Dragon(Monstruos):
    pass

class Orco(Monstruos):
    pass

class Arania(Monstruos):
    pass