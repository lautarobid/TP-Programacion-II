from datos import *
from personaje import *

def mostrar_items():
    for item in items:
        print(f'''[-]{item.nombre} 
              [TIPO]: {item.tipo} 
              [ATAQUE]:  {item.attack_power} 
              [DEFENSA]: {item.defense} 
              [EFECTO]: {item.efect}''')

def mostrar_quest():
    for quest in quests:
        print(f"Quest: {quest.name}, Completada: {quest.is_completed()}")
        print("Recompensas:")
        for reward in quest.rewards:
            print(f"- {reward.nombre}")

def menu():
    return """
    Menú:1
    1. Crear personaje
    2. Mostrar personaje con más level
    3. Mostrar guild con más puntos
    4. Buscar tu personaje completo o no la quest
    5. Gracias por ingresar a MU Rosario
    """

def crear_personaje():
    print("Creando personaje...")

def mostrar_personaje_mas_level():
    print("Mostrando personaje con más level...")

def mostrar_guild_mas_puntos():
    print("Mostrando guild con más puntos...")

def buscar_personaje_quest():
    print("Buscando tu personaje completo o no la quest...")

while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    if opt == "1":
        crear_personaje()
    elif opt == "2":
        mostrar_personaje_mas_level()
    elif opt == "3":
        mostrar_guild_mas_puntos()
    elif opt == "4":
        buscar_personaje_quest()
    elif opt == "5":
        print("Gracias por ingresar a MU Rosario.")
        break
    else:
        print("Error, Ingrese una opción válida...")
# menu
#     bola_fuego = Skill("Bola de Fuego", mana_cost=10, danio=25, cooldown=5.0)
#     tipo_personaje = TipoPersonaje("Mago")
#     tipo_personaje.add_skill(bola_fuego)
#     for skill in tipo_personaje.skills:
#         print(skill.nombre)