from datos import *

def crear_personaje():
    while True:
        nombre = input("Ingrese el nombre del personaje: ")
        if not nombre_ya_registrado(nombre):
            break
        else:
            print("El nombre ingresado ya existe. Por favor, ingrese un nuevo nombre...")
    
    while True:
        print("Seleccione el tipo de personaje: ")
        print("1. Mago")
        print("2. Caballero")
        clase = input("Ingrese el tipo de su personaje: ")
        if clase == '1':
            nuevo_personaje = Mago(nombre=nombre, tipo='Mago', nivel=1, vida=500, mana=40, fuerza=50, agilidad=8, vitalidad=12, energia=20, experiencia=200)
            break
        elif clase == '2':
            nuevo_personaje = Caballero(nombre=nombre, tipo='Caballero', nivel=1, vida=420, mana=30, fuerza=60, agilidad=9, vitalidad=18, energia=10, experiencia=150)
            break
        else:
            print("Opción no válida. Por favor, seleccione 1 o 2.")

    personajes.append(nuevo_personaje)
    return f"Personaje [{nuevo_personaje.nombre}] creado!"

def nombre_ya_registrado(nombre: str) -> bool:
    for personaje in personajes:
        if personaje.nombre == nombre:
            return True
    return False

def mostrar_articulos() -> str:
    return "\n".join([f'''
          [-]{articulo.nombre} 
          [TIPO]: {articulo.tipo} 
          [ATAQUE]:  {articulo.poder_ataque} 
          [DEFENSA]: {articulo.defensa} 
          [EFECTO]: {articulo.efecto}''' for articulo in articulos])

def mostrar_personajes() -> Personaje:
    for idx, personaje in enumerate(personajes, 1):
        print(f'''
              [{idx}]
                [NOMBRE]: {personaje.nombre}
                [TIPO]: {personaje.tipo}
                [NIVEL]: {personaje.nivel}
                [VIDA]: {personaje.vida}
                [MANA]: {personaje.mana}
                [FUERZA]: {personaje.fuerza}
                [AGILIDAD]: {personaje.agilidad}
                [VITALIDAD]: {personaje.vitalidad}
                [ENERGIA]: {personaje.energia}
                [EXPERIENCIA]: {personaje.experiencia} ''')
    while True:
        try:
            personaje_idx = int(input('Ingrese el número del personaje a elegir: ')) - 1
            if 0 <= personaje_idx < len(personajes):
                return personajes[personaje_idx]
            else:
                print("Número de personaje no válido. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def mostrar_habilidades() -> Habilidad:
    habilidades_str = "\n".join([f'''
        [{idx}]
        [HABILIDAD]: {habilidad.nombre} 
        [MANA]: {habilidad.mana_costo} 
        [DAÑO]:  {habilidad.danio} 
        [ENFRIAMIENTO]: {habilidad.enfriamiento}''' for idx, habilidad in enumerate(habilidades, 1)])
    print(habilidades_str)
    while True:
        try:
            habilidad_idx = int(input("Ingrese el número de la habilidad que desea usar: ")) - 1
            if 0 <= habilidad_idx < len(habilidades):
                return habilidades[habilidad_idx]
            else:
                print("Número de habilidad no válido. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def mostrar_monstruos() -> Monstruos:
    monstruos_str = "\n".join([f'''
        [{idx}]
        [NOMBRE]: {monstruos.nombre} 
        [TIPO]: {monstruos.tipo} 
        [VIDA]:  {monstruos.vida} 
        [ATAQUE]:  {monstruos.ataque}             
        [DEFENSA]:  {monstruos.defensa} 
        [VELOCIDAD]: {monstruos.velocidad}''' for idx, monstruos in enumerate(lista_monstruos, 1)])
    print(monstruos_str)
    while True:
        try:
            monstruos_idx = int(input("Ingrese el número del monstruo a elegir: ")) - 1
            if 0 <= monstruos_idx < len(lista_monstruos):
                return lista_monstruos[monstruos_idx]
            else:
                print("Número de monstruo no válido. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def mostrar_misiones() -> Mision:
    misiones_str = "\n".join([f'''
        [{idx}]
        [MISION]: {mision.nombre} 
        [DESCRIPCION]: {mision.descripcion}
        [RECOMPENSA]:  {mision.recompensa.nombre}''' for idx, mision in enumerate(lista_mision, 1)])
    print(misiones_str)
    while True:
        try:
            mision_idx = int(input('Ingrese el número de la quest: ')) - 1
            if 0 <= mision_idx < len(lista_mision):
                return lista_mision[mision_idx]
            else:
                print("Número de misión no válido. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def mostrar_inventario(personaje_seleccionado) -> str:
    inventario_str = "\n".join([f'''
        [NOMBRE]: {personaje_seleccionado.nombre}
        [INVENTARIO]: {", ".join([str(articulo) for articulo in personaje_seleccionado.equipamiento]) if personaje_seleccionado.equipamiento else "El inventario está vacío."}\n'''])
    return inventario_str

def menu() -> str:
    return """
    Menú:
    1. Crear Personaje
    2. Elegir Personaje
    3. Salir de MU Rosario
    """

def menu2() -> str:
    return """
    Menú:
    1. Mostrar Misiones
    2. Mostrar Articulos
    3. Mostrar Inventario
    4. Pelear
    5. Salir
    """

def main():
    contador_dragones = 0
    contador_orcos = 0
    contador_aranias = 0
    
    while True:
        print(menu())
        opt = input("Ingrese la opción seleccionada: ")
        if opt == "1":
            mensaje = crear_personaje()
            print(mensaje)
        elif opt == "2":
            personaje_seleccionado = mostrar_personajes()
            print("El personaje elegido es: ", personaje_seleccionado.nombre)
            while True:
                input("Presione ENTER para continuar...")
                print(menu2())
                num = input("Ingrese la opción seleccionada: ")
                if num == "1":
                    mision_seleccionada = mostrar_misiones()
                    print(mision_seleccionada)
                    print("-------------------------------------------------------------------------------------")
                elif num == "2":
                    print(mostrar_articulos())
                    print("-------------------------------------------------------------------------------------")
                elif num == "3":
                    print(mostrar_inventario(personaje_seleccionado))
                elif num == "4":
                    monstruo_seleccionado = mostrar_monstruos()
                    habilidad_seleccionada = mostrar_habilidades()
                    resultado_pelea = monstruo_seleccionado.pelea(personaje_seleccionado, habilidad_seleccionada)
                    print(resultado_pelea)

                    if monstruo_seleccionado == lista_monstruos[0]:
                        contador_dragones += 1
                        print(f"Dragones derrotados: {contador_dragones}")
                    elif monstruo_seleccionado == lista_monstruos[1]:
                        contador_aranias += 1
                        print(f"Arañas derrotadas: {contador_aranias}")
                    elif monstruo_seleccionado == lista_monstruos[2]:
                        contador_orcos += 1
                        print(f"Orcos derrotados: {contador_orcos}")
                    print("-------------------------------------------------------------------------------------")

                    if contador_dragones == 3 and not mision1.esta_completada():
                        print(f"Felicidades, has completado la misión {mision1.nombre}")
                        mision1.mision_completada()
                        print(f"Tu recompensa es: {mision1.recompensa.nombre}")
                        personaje_seleccionado.equipar_articulo(mision1.recompensa)
                    elif contador_aranias == 3 and not mision2.esta_completada():
                        print(f"Felicidades, has completado la misión {mision2.nombre}")
                        mision2.mision_completada()
                        print(f"Tu recompensa es: {mision2.recompensa.nombre}")
                        personaje_seleccionado.equipar_articulo(mision2.recompensa)
                    elif contador_orcos == 3 and not mision3.esta_completada():
                        print(f"Felicidades, has completado la misión {mision3.nombre}")
                        mision3.mision_completada()
                        print(f"Tu recompensa es: {mision3.recompensa.nombre}")
                        personaje_seleccionado.equipar_articulo(mision3.recompensa)
                elif num == "5":
                    print("Gracias por elegir MU Rosario.")
                    break
                else:
                    print("Error, ingrese una opción válida...")
        elif opt == "3":
            print("Gracias por elegir MU Rosario.")
            break
        else:
            print("Error, ingrese una opción válida...")

if __name__ == "__main__":
    main()