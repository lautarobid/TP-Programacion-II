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
    def nombre(self, new_nombre:str):
        self.__nombre = new_nombre


    def subir_nivel(self):
        self.__nivel += 1
        self.__vida += 10
        self.__mana += 5
        self.__fuerza += 2
        self.__agilidad += 2
        self.__vitalidad += 3
        self.__energia += 2
        print(f"{self.__nombre} subio de nivel a: {self.__nivel}!")
    

    def equipar_item(self, articulo: Articulo):
        self.__equipamiento.append(Articulo)
        print(f"{self.__nombre} equipado {articulo.__nombre}.")

    def desequipar_item(self, articulo: Articulo):
        if articulo in self.__equipamiento:
            self.__equipamiento.remove(articulo)
            print(f"{self.__nombre} desequipado {articulo.__nombre}.")

    @classmethod
    def __validar_nombre(cls, nombre:str):
        if nombre in cls.__nombres_registrados:
            raise RuntimeError('ERROR- NOMBRE REGISTRADO')
        cls.__nombres_registrados.add(nombre)
        return nombre