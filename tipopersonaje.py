from skill import Skill
from item import Item
class TipoPersonaje():
    def __init__(self,nombre:str):
        self.__nombre = nombre
        self.__skills = []
    
    @property
    def nombre(self)->str:
        return self.__nombre
    
    @nombre.setter
    def set_nombre (self,new_nombre:str)-> None:
        self.__nombre = new_nombre

    @property 
    def skills(self) -> list:
        return self.__skills
    
    def add_skills(self, skill: Skill) -> None:
        self.__skills.append(skill)
        print(f'Habilidad {skill.nombre} fue añadida a {self.nombre}') 