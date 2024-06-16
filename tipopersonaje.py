from skill import Skill
class TipoPersonaje():
    def __init__(self,nombre:str):
         self.__nombre = nombre
    
    @property
    def nombre(self)->str:
        return self.__nombre
    @nombre.setter
    def set_nombre (self,new_nombre:str)-> None:
        self.__nombre = new_nombre