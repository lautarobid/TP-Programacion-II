from datos import *

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

def menu ():
    return "\n1 - Crear Personaje \n2 - Ranking Personaje\n3 - Ranking Guilds\n4 - Salir"

while True:

    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")

    if opt == "1":
        pass
    
    elif opt == "2":
        mostrar_items()
    elif opt == "3":
        mostrar_quest()

    elif opt == "4":
        print("Gracias por utilizar nuestro sistema.")
        break

    else:
        print("Error, Ingrese una opcion valida...")

# menu
#     bola_fuego = Skill("Bola de Fuego", mana_cost=10, danio=25, cooldown=5.0)
#     tipo_personaje = TipoPersonaje("Mago")
#     tipo_personaje.add_skill(bola_fuego)
#     for skill in tipo_personaje.skills:
#         print(skill.nombre)