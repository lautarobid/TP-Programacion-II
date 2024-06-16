from abc import ABC,classmethod
from tipopersonaje import TipoPersonaje

class Personaje(ABC):
    def __init__(self, name: str, level: int, health: int, mana: int, strength: int, agility: int, vitality: int, energy: int, experience: int):
        self.name = name
        self.level = level
        self.health = health
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.vitality = vitality
        self.energy = energy
        self.experience = experience
        self.equipment: List[Item] = []

    @abstractmethod
    def attack(self, target: 'Personaje'):
        pass

    @abstractmethod
    def use_skill(self, skill: Skill, target: 'Personaje'):
        pass

    def level_up(self):
        self.level += 1
        self.health += 10
        self.mana += 5
        self.strength += 2
        self.agility += 2
        self.vitality += 3
        self.energy += 2
        print(f"{self.name} leveled up to {self.level}!")

    def equip_item(self, item: Item):
        self.equipment.append(item)
        print(f"{self.name} equipped {item.name}.")

    def unequip_item(self, item: Item):
        if item in self.equipment:
            self.equipment.remove(item)
            print(f"{self.name} unequipped {item.name}.")

class Wizard(Character):
    def attack(self, target: 'Character'):
        damage = self.energy * 2
        target.health -= damage
        print(f"{self.name} attacks {target.name} causing {damage} damage.")

    def use_skill(self, skill: Skill, target: 'Character'):
        skill.cast(self, target)

class Knight(Character):
    def attack(self, target: 'Character'):
        damage = self.strength * 1.5
        target.health -= damage
        print(f"{self.name} attacks {target.name} causing {damage} damage.")

    def use_skill(self, skill: Skill, target: 'Character'):
        skill.cast(self, target)
