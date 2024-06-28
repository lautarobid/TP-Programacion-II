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
    print("2. Caballero")
    clase = input("Ingrese el tipo de su personaje: ")
    if clase == '1':
        nuevo_personaje = Personaje(nombre=nombre, nivel= 1, vida=500, mana=40, fuerza=50, agilidad=8, vitalidad=12, energia=20, experiencia=200)
    elif clase == '2':
        nuevo_personaje = Personaje(nombre=nombre, nivel=1,  vida=420, mana=30, fuerza=60, agilidad=9, vitalidad=18, energia=10, experiencia=150)
    personajes.append(nuevo_personaje)
    print(f"Personaje [{nuevo_personaje.nombre}] creado!")
    return nuevo_personaje

def nombre_ya_registrado(nombre: str) -> bool:
    for personaje in personajes:
        if personaje.nombre == nombre:
            return True
    return False

def mostrar_articulos():
    for articulo in articulos:
        print(f'''
              [-]{articulo.nombre} 
              [TIPO]: {articulo.tipo} 
              [ATAQUE]:  {articulo.poder_ataque} 
              [DEFENSA]: {articulo.defensa} 
              [EFECTO]: {articulo.efecto}''')

def mostrar_personajes():
    for idx, personaje in enumerate(personajes,1):
        print(f'''
              [{idx}]
                [NOMBRE]: {personaje.nombre}
                [NIVEL]: {personaje.nivel}
                [HEALTH]: {personaje.vida}
                [MANA]: {personaje.mana}
                [FUERZA]: {personaje.fuerza}
                [AGILIDAD]: {personaje.agilidad}
                [VITALIDAD]: {personaje.vitalidad}
                [ENERGIA]: {personaje.energia}
                [EXPERIENCIA]: {personaje.experiencia} ''')
    personaje_idx = int(input('Ingrese el numero del personaje a elegir: '))-1
    return personajes[personaje_idx]

        
def mostrar_habilidades():
    for idx, habilidad in enumerate(habilidades, 1): 
            print(f'''
            [{idx}]
            [HABILIDAD]: {habilidad.nombre} 
            [MANA]: {habilidad.mana_costo} 
            [DAÑO]:  {habilidad.danio} 
            [COOLDOWN]: {habilidad.enfriamiento}''')
    habilidad_idx = int(input("Ingrese el numero de la habilidad que desea usar: ")) - 1
    return habilidades[habilidad_idx]

def mostrar_monstruos():
    for idx, monstruos in enumerate(lista_monstruos, 1): 
            print(f'''
            [{idx}]
            [NOMBRE]: {monstruos.nombre} 
            [TIPO]: {monstruos.tipo} 
            [VIDA]:  {monstruos.vida} 
            [ATAQUE]:  {monstruos.ataque}             
            [DEFENSA]:  {monstruos.defensa} 
            [VELOCIDAD]: {monstruos.velocidad}''')
    monstruos_idx = int(input("Ingrese el numero del monstruo a elegir: ")) -1
    return lista_monstruos[monstruos_idx]

def mostrar_misiones():
    for idx, mision in enumerate(lista_mision, 1): 
        print(f'''
            [{idx}]
            [QUEST]: {mision.nombre} 
            [DESCRIPCION]: {mision.descripcion}
            [RECOMPENSA]:  {mision.recompensa}''')
        print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    mision_idx = int(input('Ingrese el numero de la quest: '))-1
    return lista_mision[mision_idx]

def mostrar_inventario():
    for personaje in personajes:
        print(f'''
            [NOMBRE]: {personaje.nombre}
            [INVENTARIO]: ''')
        if personaje.__equipamiento:
            for articulos in personaje.__equipamiento:
                print(f"\n{articulos}")
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
        print("El personaje elegido es: ", personaje_seleccionado.nombre)
        while True:
            input("Presione ENTER para continuar...")
            print(menu2())
            num = input("Ingrese la opcion seleccionada: ")
            if num == "1":
                mostrar_misiones()
                print("-------------------------------------------------------------------------------------")
            elif num == "2":
                mostrar_articulos()
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
                    if mision1.esta_completada():
                        print("La mision ya fue completada.")
                    else:
                        print(f"Felicidades, has completado la mision {mision1.nombre}")
                        mision1.mision_completada()
                        print(f"Tu recompensa es: {mision1.recompensa}")
                        personaje_seleccionado.equipar_articulo(mision1.recompensa)
                elif contador_aranias == 3:
                    print(f"Felicidades, has completado la mision {mision2.nombre}")
                    mision2.mision_completada()
                    print(f"Tu recompensa es: {mision2.recompensa}")
                    personaje_seleccionado.equipar_articulo(mision2.recompensa)
                elif contador_orcos == 3:
                    print(f"Felicidades, has completado la mision {mision3.nombre}")
                    mision3.mision_completada()
                    print(f"Tu recompensa es: {mision3.recompensa}")
                    personaje_seleccionado.equipar_articulo(mision3.recompensa)                  
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