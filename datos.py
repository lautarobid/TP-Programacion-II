from personaje import Wizard, Knight
from skill import Skill
from item import Item
from quest import Quest
from monstruos import Monstruos


#creo personajes
rune = Wizard('Rune Wizard', nivel=7, health=100, mana=40, fuerza=5, agilidad=8, vitalidad=12, energia=20, experience=200)
blade = Knight('Blade Knight', nivel=9, health=120, mana=30, fuerza=10, agilidad=9, vitalidad=18, energia=10, experience=150)

#creo habilidad
bola_fuego = Skill('Bola de fuego', mana_cost=10, danio=25, cooldown=5.0)
bola_hielo = Skill('Bola de hielo', mana_cost=12, danio=20, cooldown=6.0)
rayo = Skill('Rayo', mana_cost=8, danio=20, cooldown=4.0)

habilidades = [bola_fuego, bola_hielo, rayo]
#personaje usa habilidad
# rune.use_skill(bola_fuego, blade)  
# blade.use_skill(curar, blade) 
# rune.use_skill(escudo, rune) 

#items
items = [
    Item(nombre='Espada', tipo='Arma', attack_power=50, defense=50, efect='Aumenta velocidad de ataque'),
    Item(nombre='Arco', tipo='Arma', attack_power=40, defense=5, efect='Aumenta la precision'),
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

# monstruos
dragon = Monstruos('Dragon', 'Fuego', 100, 20, 10, 5)
arania = Monstruos('Arania', 'Veneno', 50, 10, 5, 10)
orco = Monstruos('Orco', 'Fuerza', 80, 15, 8, 8)

lista_monstruos = [dragon, arania, orco]