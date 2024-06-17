<<<<<<< HEAD
Personaje = []
=======
from personaje import Wizard, Knight
from skill import Skill
from item import Item
from quest import Quest


#creo personajes
rune = Wizard('Rune Wizard', nivel=7, health=100, mana=40, fuerza=5, agilidad=8, vitalidad=12, energia=20, experience=200)
blade = Knight('Blade Knight', nivel=9, health=120, mana=30, fuerza=10, agilidad=9, vitalidad=18, energia=10, experience=150)

#creo habilidad
bola_fuego = Skill('Bola de fuego', mana_cost=10, danio=25, cooldown=5.0)
escudo = Skill('Escudo', mana_cost=12, danio=0, cooldown=6.0)
curar = Skill('Curacion', mana_cost=8, danio=-20, cooldown=4.0)

#personaje usa habilidad
rune.use_skill(bola_fuego, blade)  
blade.use_skill(curar, blade) 
rune.use_skill(escudo, rune) 

#items
items = [
    Item(nombre='Espada', tipo='arma', attack_power=50, defense=50, efect='Aumenta velocidad de ataque'),
    Item(nombre='Arco', tipo='arma', attack_power=40, defense=5, efect='Aumenta la precision'),
    Item(nombre='armadura', tipo='Defensa', attack_power=5, defense=45, efect='Regenera salud'),
    Item(nombre='Pocion de Fuerza', tipo='Consumible', attack_power=20, defense=0, efect='Aumenta el ataque temporalmente'),
    Item(nombre='Pocion de Resistencia', tipo='Consumible', attack_power=0, defense=20, efect='Aumenta la defensa temporalmente'),
]

# crear quests
quest1 = Quest(name="La espada perdida", description="Encuentra y recupera la espada legendaria.", rewards=[items[0]])
quest2 = Quest(name="Defiende el pueblo", description="Protege el pueblo del ataque de los goblins.", rewards=[items[2]])
quest3 = Quest(name="Recolecta hierbas", description="Recolecta hierbas para crear pociones.", rewards=[items[3], items[4]])

# lista de quests
quests = [quest1, quest2, quest3]

# completar una quest
quest1.complete_quest()
>>>>>>> 28ca59e3c8e64e7dd7a8e00dd302c7f997dbe2f8
