
class Skill():
    def __init__(self,nombre:str,mana_cost:int,danio:int,cooldown:float):
        self.__nombre = nombre
        self.__mana_cost = mana_cost
        self.__danio = danio
        self.__cooldown = cooldown
    
    @property
    def nombre(self)->str:
        return self.__nombre
    @nombre.setter
    def nombre (self,new_nombre:str)-> None:
        self.__nombre = new_nombre
        
    @property
    def mana_cost(self)->int:
        return self.__mana_cost
    @mana_cost.setter
    def mana_cost(self,new_mana_cost:int)-> None:
        self.__mana_cost = new_mana_cost
    
    @property
    def danio(self)->int:
        return self.__danio
    
    @danio.setter
    def danio(self,new_danio:int)-> None:
        self.__danio = new_danio
    
    @property
    def cooldown(self)->float:
        return self.__cooldown
    @cooldown.setter
    def cooldown (self,new_cooldown:float)-> None:
        self.__cooldown = new_cooldown

    # def cast(self, caster, target) -> None:
    #     if caster.mana >= self.__mana_cost:
    #         caster.mana -= self.__mana_cost
    #         target.health -= self.__danio
    #         print(f'{caster.nombre} lanza {self.__nombre} a {target.nombre}, causando {self.__danio} daño')
    #     else:
    #         print(f'{caster.nombre} no tiene suficiente mana para lanzar {self.__nombre}')
    # #tengo que pasar en skill dos cosas: el personaje que lanza casster y el personaje que recibe: target.
    # # si caster tiene suficieinte mana para lanzar la habilidad se reeduce su mana y se aplizca el daño a target y algo del tiempo 