from personaje import Wizard, Knight
from skill import Skill

#creo personaje
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