

class Skill():
    def __init__(self,nombre:str,mana_cost:int,damage:int,cooldown:float):
         self.__nombre = nombre
         self.__mana_cost = mana_cost
         self.__damage = damage
         self.__cooldown = cooldown
    
    @property
    def nombre(self)->str:
        return self.__nombre
    @nombre.setter
    def set_nombre (self,new_nombre:str)-> None:
        self.__nombre = new_nombre
        
    @property
    def mana_cost(self)->int:
        return self.__mana_cost
    @mana_cost.setter
    def set__mana_cost (self,new_mana_cost:int)-> None:
        self.__mana_cost = new_mana_cost
    
    @property
    def damage(self)->int:
        return self.__damage
    @damage.setter
    def set__damage (self,new_damage:int)-> None:
        self.__damage = new_damage
    
    @property
    def cooldown(self)->float:
        return self.__cooldown
    @cooldown.setter
    def set__cooldown (self,new_cooldown:float)-> None:
        self.__cooldown = new_cooldown