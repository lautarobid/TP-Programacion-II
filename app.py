def menu ():
    return "\n1 - Crear Personaje\n2 - Ranking Personaje\n3 - Ranking Guilds\n4 - Salir"

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

