from abc import ABC, abstractmethod
from typing import List
from articulo import Articulo

class Personaje(ABC):

    __nombres_registrados = set()

    def __init__(self, nombre: str, nivel: int, vida: int, mana: int, fuerza: int, agilidad: int, vitalidad: int, energia: int, experiencia: int):
        self.__nombre = Personaje.__validar_nombre(nombre)
        self.__nivel = nivel
        self.__vida = vida
        self.__mana = mana
        self.__fuerza = fuerza
        self.__agilidad = agilidad
        self.__vitalidad = vitalidad
        self.__energia = energia
        self.__experiencia = experiencia
        self.__equipamiento: List[Articulo] = []

    @property 
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre: str):
        self.__nombre = Personaje.__validar_nombre(new_nombre)
        
    @property 
    def nivel(self) -> int:
        return self.__nivel
    
    @nivel.setter
    def nivel(self, new_nivel: int):
        self.__nivel = new_nivel
        
    @property 
    def vida(self) -> int:
        return self.__vida
    
    @vida.setter
    def vida(self, new_vida: int):
        self.__vida = new_vida
        
    @property 
    def mana(self) -> int:
        return self.__mana
    
    @mana.setter
    def mana(self, new_mana: int):
        self.__mana = new_mana
        
    @property 
    def fuerza(self) -> int:
        return self.__fuerza
    
    @fuerza.setter
    def fuerza(self, new_fuerza: int):
        self.__fuerza = new_fuerza
        
    @property 
    def agilidad(self) -> int:
        return self.__agilidad
    
    @agilidad.setter
    def agilidad(self, new_agilidad: int):
        self.__agilidad = new_agilidad
        
    @property 
    def vitalidad(self) -> int:
        return self.__vitalidad
    
    @vitalidad.setter
    def vitalidad(self, new_vitalidad: int):
        self.__vitalidad = new_vitalidad
        
    
    @property 
    def energia(self) -> int:
        return self.__energia
    
    @energia.setter
    def energia(self, new_energia: int):
        self.__energia = new_energia
        
    @property 
    def experiencia(self) -> int:
        return self.__experiencia
    
    @experiencia.setter
    def experiencia(self, new_experiencia: int):
        self.__experiencia = new_experiencia
        

    def subir_nivel(self):
        self.__nivel += 1
        self.__vida += 10
        self.__mana += 5
        self.__fuerza += 2
        self.__agilidad += 2
        self.__vitalidad += 3
        self.__energia += 2
        print(f"{self.nombre} subio de nivel a: {self.nivel}!")
    

    def equipar_articulo(self, articulo: Articulo):
        self.__equipamiento.append(articulo)
        print(f"{self.nombre} equipado {articulo.nombre}.")

    def desequipar_articulo(self, articulo: Articulo):
        if articulo in self.__equipamiento:
            self.__equipamiento.remove(articulo)
            print(f"{self.nombre} desequipado {articulo.nombre}.")

    @classmethod
    def __validar_nombre(cls, nombre:str):
        if nombre in cls.__nombres_registrados:
            raise RuntimeError('ERROR- NOMBRE REGISTRADO')
        cls.__nombres_registrados.add(nombre)
        return nombre
    
    def _str_(self) -> str:
        return f'''
        Nombre: {self.nombre}
        Nivel: {self.nivel}
        Vida: {self.vida}
        Mana: {self.mana}
        Fuerza: {self.fuerza}
        Agilidad: {self.agilidad}
        Vitalidad: {self.vitalidad}
        Energia: {self.energia}
        Experiencia: {self.experiencia}'''