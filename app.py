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
    for idx, personaje in enumerate(personajes,1):
        print(f'''
              [{idx}]
                [NOMBRE]: {personaje.nombre}
                [NIVEL]: {personaje.nivel}
                [HEALTH]: {personaje.health}
                [MANA]: {personaje.mana}
                [FUERZA]: {personaje.fuerza}
                [AGILIDAD]: {personaje.agilidad}
                [VITALIDAD]: {personaje.vitalidad}
                [ENERGIA]: {personaje.energia}
                [EXPERIENCIA]: {personaje.experience} ''')
    personaje_idx = int(input('Ingrese el numero del personaje a elegir: '))-1
    return personajes[personaje_idx]

        
def mostrar_habilidades():
    for idx, habilidad in enumerate(habilidades, 1): 
            print(f'''
            [{idx}]
            [HABILIDAD]: {habilidad.nombre} 
            [MANA]: {habilidad.mana_cost} 
            [DAÑO]:  {habilidad.danio} 
            [COOLDOWN]: {habilidad.cooldown}''')
    habilidad_idx = int(input("Ingrese el numero de la habilidad que desea usar: ")) - 1
    return habilidades[habilidad_idx]

def mostrar_monstruos():
    for idx, monster in enumerate(lista_monstruos, 1): 
            print(f'''
            [{idx}]
            [NOMBRE]: {monster.nombre} 
            [TIPO]: {monster.tipo} 
            [VIDA]:  {monster.vida} 
            [ATAQUE]:  {monster.ataque}             
            [DEFENSA]:  {monster.defensa} 
            [VELOCIDAD]: {monster.velocidad}''')
    monster_idx = int(input("Ingrese el numero del monstruo a elegir: ")) -1
    return lista_monstruos[monster_idx]

def mostrar_quest():
    for idx, quest in enumerate(lista_quest, 1): 
        print(f'''
            [{idx}]
            [QUEST]: {quest.name} 
            [DESCRIPCION]: {quest.description}
            [RECOMPENSA]:  {quest.rewards}''')
        print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    quest_idx = int(input('Ingrese el numero de la quest: '))-1
    return lista_quest[quest_idx]

def mostrar_inventario():
    for personaje in personajes:
        print(f'''
            [NOMBRE]: {personaje.nombre}
            [INVENTARIO]: ''')
        if personaje.equipment:
            for item in personaje.equipment:
                print(f"\n{item}")
        else:
            print("El inventario está vacío.")

def menu():
    return """
    Menú:
    1. Crear Personaje
    2. Elegir Personaje
    3. Salir de MU Rosario
    """
    
def menu2():
    return """
    Menú:
    1. Mostrar Quest
    2. Mostrar Items
    3. Mostrar Inventario
    4. Pelear
    5. Salir
    """

while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    if opt == "1":
        crear_personaje()
    elif opt == "2":
        personaje_seleccionado = mostrar_personajes()
        print("El personaje elegido es: ", personaje_seleccionado)
        while True:
            input("Presione ENTER para continuar...")
            print(menu2())
            num = input("Ingrese la opcion seleccionada: ")
            if num == "1":
                mostrar_quest()
                print("-------------------------------------------------------------------------------------")
            elif num == "2":
                mostrar_items()
                print("-------------------------------------------------------------------------------------")
            elif num == "3":
                mostrar_inventario()
            elif num == "4":
                monstruo_seleccionado = mostrar_monstruos()
                habilidad_seleccionada = mostrar_habilidades()
                Monstruos.pelea(monstruo_seleccionado, personaje_seleccionado, habilidad_seleccionada)

                if monstruo_seleccionado == lista_monstruos[0]:
                    contador_dragones += 1
                    print(f"Dragones derrotados: {contador_dragones}")
                elif monstruo_seleccionado == lista_monstruos[1]:
                    contador_aranias += 1
                    print(f"Arañas derrotados: {contador_aranias}")
                elif monstruo_seleccionado == lista_monstruos[2]:
                    contador_orcos += 1
                    print(f"Orcos derrotados: {contador_orcos}")
                print("-------------------------------------------------------------------------------------")

                if contador_dragones == 3:
                    if quest1.is_completed():
                        print("La mision ya fue completada.")
                    else:
                        print(f"Felicidades, has completado la mision {quest1.name}")
                        quest1.complete_quest()
                        print(f"Tu recompensa es: {quest1.rewards}")
                        personaje_seleccionado.equipar_item(quest1.rewards)
                elif contador_aranias == 3:
                    print(f"Felicidades, has completado la mision {quest2.name}")
                    quest2.complete_quest()
                    print(f"Tu recompensa es: {quest2.rewards}")
                    personaje_seleccionado.equipar_item(quest2.rewards)
                elif contador_orcos == 3:
                    print(f"Felicidades, has completado la mision {quest3.name}")
                    quest3.complete_quest()
                    print(f"Tu recompensa es: {quest3.rewards}")
                    personaje_seleccionado.equipar_item(quest3.rewards)                  
            elif num == "5":
                print("Gracias por elegir MU Rosario.")
                break
            else:
                print("Error, Ingrese una opción válida...")

    elif opt == "3":
        print("Gracias por elegir MU Rosario.")
        break
    else:
        print("Error, Ingrese una opción válida...")