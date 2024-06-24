from datos import *

def crear_personaje():
    while True:
        nombre = input("Ingrese el nombre del personaje: ")
        if not nombre_ya_registrado(nombre):
            break
        else:
            print("El nombre ingresado ya existe. Por favor, ingrese un nuevo nombre...")
    
    print("Seleccione el tipo de personaje: ")
    print("1. Mago")
    print("2. Guerrero")
    clase = input("Ingrese el tipo de su personaje: ")
    if clase == '1':
        nuevo_personaje = Wizard(nombre=nombre, nivel= 1, health=500, mana=40, fuerza=50, agilidad=8, vitalidad=12, energia=20, experience=200)
    elif clase == '2':
        nuevo_personaje = Knight(nombre=nombre, nivel=1,  health=420, mana=30, fuerza=60, agilidad=9, vitalidad=18, energia=10, experience=150)
    personajes.append(nuevo_personaje)
    print(f"Personaje [{nuevo_personaje.nombre}] creado!")
    return nuevo_personaje

def nombre_ya_registrado(nombre: str) -> bool:
    for personaje in personajes:
        if personaje.nombre == nombre:
            return True
    return False

def mostrar_items():
    for item in items:
        print(f'''
              [-]{item.nombre} 
              [TIPO]: {item.tipo} 
              [ATAQUE]:  {item.attack_power} 
              [DEFENSA]: {item.defense} 
              [EFECTO]: {item.efect}''')

def mostrar_personajes():
    for personaje in personajes:
        print(f'''
                [NOMBRE]: {personaje.nombre}
                [NIVEL]: {personaje.nivel}
                [HEALTH]: {personaje.health}
                [MANA]: {personaje.mana}
                [FUERZA]: {personaje.fuerza}
                [AGILIDAD]: {personaje.agilidad}
                [VITALIDAD]: {personaje.vitalidad}
                [ENERGIA]: {personaje.energia}
                [EXPERIENCIA]: {personaje.experience}
                [EQUIPO]: ''')
        
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
    1. Crear Personaje
    2. ---
    3. Mostrar personajes
    4. Mostrar items
    5. Pelear
    6. Gracias por ingresar a MU Rosario
    """
    
while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    if opt == "1":
       crear_personaje()
    elif opt == "2":
        pass
    elif opt == "3":
        mostrar_personajes()
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
