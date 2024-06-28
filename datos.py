from caballero import Caballero
from mago import Mago
from habilidad import Habilidad
from articulo import Articulo
from mision import Mision
from monstruos import Monstruos
from personaje import Personaje

# Creo personajes
mago = Personaje(nombre='Mago', nivel=7, vida=100, mana=40, fuerza=5, agilidad=8, vitalidad=12, energia=20, experiencia=200)
caballero = Personaje(nombre='Caballero', nivel=9, vida=120, mana=30, fuerza=10, agilidad=9, vitalidad=18, energia=10, experiencia=150)

personajes = [mago, caballero]

# Creo habilidades
bola_fuego = Habilidad('Bola de fuego', mana_costo=10, danio=25, enfriamiento=5.0)
bola_hielo = Habilidad('Bola de hielo', mana_costo=12, danio=20, enfriamiento=6.0)
rayo = Habilidad('Rayo', mana_costo=8, danio=20, enfriamiento=4.0)

habilidades = [bola_fuego, bola_hielo, rayo]

# Creo artículos
articulos = [
    Articulo(nombre='Espada legendaria', tipo='Arma', poder_ataque=50, defensa=10, efecto='Aumenta fuerza'),
    Articulo(nombre='Escudo legendario', tipo='Defensa', poder_ataque=5, defensa=50, efecto='Aumenta defensa'),
    Articulo(nombre='Armadura legendaria', tipo='Armadura', poder_ataque=0, defensa=100, efecto='Aumenta vida'),
]

# Creo misiones
mision1 = Mision(nombre="La espada perdida", descripcion="Encuentra y recupera la espada legendaria matando 3 dragones", recompensa=articulos[0])
mision2 = Mision(nombre="Defiende el pueblo", descripcion="Protege el pueblo del ataque de las arañas. Mata 3 arañas", recompensa=articulos[1])
mision3 = Mision(nombre="La invasión", descripcion="Detiene a los orcos. Mata 3 orcos.", recompensa=articulos[2])

lista_mision = [mision1, mision2, mision3]

# Creo monstruos
dragon = Monstruos('Dragon', 'Fuego', 100, 20, 10, 5)
arania = Monstruos('Arania', 'Veneno', 50, 10, 5, 10)
orco = Monstruos('Orco', 'Fuerza', 80, 15, 8, 8)

lista_monstruos = [dragon, arania, orco]

contador_dragones = 0
contador_orcos = 0
contador_aranias = 0