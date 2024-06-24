from datos import *

def mostrar_items():
    for item in items:
        print(f'''
              [-]{item.nombre} 
              [TIPO]: {item.tipo} 
              [ATAQUE]:  {item.attack_power} 
              [DEFENSA]: {item.defense} 
              [EFECTO]: {item.efect}''')
        
def mostrar_habilidades():
    for habilidad in habilidades: 
            print(f'''
            [HABILIDAD]: {habilidad.nombre} 
            [MANA]: {habilidad.mana_cost} 
            [DAÑO]:  {habilidad.danio} 
            [COOLDOWN]: {habilidad.cooldown}''')
    habilidad = input("Ingrese el numero de habilidad que desea usar: ")
    if habilidad == '1':
        habilidad_seleccionada = habilidades[0]
    elif habilidad == '2':
        habilidad_seleccionada = habilidades[1]
    elif habilidad == '3':
        habilidad_seleccionada = habilidades[2]
    return habilidad_seleccionada

def mostrar_monstruos():
    for monster in lista_monstruos: 
            print(f'''
            [NOMBRE]: {monster.nombre} 
            [TIPO]: {monster.tipo} 
            [VIDA]:  {monster.vida} 
            [ATAQUE]:  {monster.ataque}             
            [DEFENSA]:  {monster.defensa} 
            [VELOCIDAD]: {monster.velocidad}''')
    monster = input("Ingrese el numero de habilidad que desea usar: ")
    if monster == '1':
        mounstro_seleccionado = lista_monstruos[0]
    elif monster == '2':
        mounstro_seleccionado = lista_monstruos[1]
    elif monster == '3':
        mounstro_seleccionado = lista_monstruos[2]
    return mounstro_seleccionado

def mostrar_quest():
    for quest in quests:
        print(f"Quest: {quest.name}, Completada: {quest.is_completed()}")
        print("Recompensas:")
        for reward in quest.rewards:
            print(f"- {reward.nombre}")

def menu():
    return """
    Menú:
    1. --
    2. ---
    3. --
    4. Mostrar items
    5. Pelear
    6. Gracias por ingresar a MU Rosario
    """
    
while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    if opt == "1":
       pass
    elif opt == "2":
        pass
    elif opt == "3":
        pass
    elif opt == "4":
       mostrar_items()
    elif opt == "5":
        habilidad_seleccionada = mostrar_habilidades()
        monstruo_seleccionado = mostrar_monstruos()
        Monstruos.pelea(monstruo_seleccionado, rune, habilidad_seleccionada)
    elif opt == "6":
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