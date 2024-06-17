from datos import *
from item import Item

def mostrar_items():
    for item in enumerate(items,1):
        print(f'{item} - {item.nombre} - {item.tipo} {item.efect}')

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
        pass

    elif opt == "4":
        print("Gracias por utilizar nuestro sistema.")
        break

    else:
        print("Error, Ingrese una opcion valida...")