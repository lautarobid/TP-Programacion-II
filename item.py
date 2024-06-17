

class Item():
    item = []
    
    def __init__(self,nombre:str,tipo:str,attack_power:int,defense:int,efect:str):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__attack_power = attack_power
        self.__defense = defense
        self.__efect: efect
    
    @property
    def nombre(self)->str:
        return self.__nombre
    
    @nombre.setter
    def set_nombre (self,new_nombre:str)-> None:
        self.__nombre = new_nombre

    @property
    def tipo(self)->str:
        return self.__tipo
    
    @tipo.setter
    def set_tipo (self,new_tipo:str)-> None:
        self.__tipo = new_tipo

    @property
    def attack_power(self)->int:
        return self.__attack_power
    
    @attack_power.setter
    def set_attack_power (self,new_attack_power:int)-> None:
        self.__attack_power = new_attack_power

    @property
    def defense(self)->int:
        return self.__defense
    
    @defense.setter
    def set_defense (self,new_defense:int)-> None:
        self.__defense = new_defense  

    @property
    def efect(self)->str:
        return self.__efect
    
    @efect.setter
    def set_efect (self,new_efect:str)-> None:
        self.__efect = new_efect  
