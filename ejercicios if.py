print("Bienvenido al castillo enbrujado")
opciones = int(input("Elije una de estas 4 puertas y se decidira tu futoro: 1 puerta roja grande, 2 puerta negra pequeña, 3 puerta verde esmeralda, 4 puerta de celda pero detras hay una niebla que no te deja ver "))
if opciones == 1:
    print("Has elegido la puerta roja grande")
    decision = int(input("Dentro de esta puerta encuentras un pozo. ¿Qué decides? 1: tirarme, 2: no tirarme "))
    if decision == 1:
        print("game over")
    elif decision == 2:
        print("sigues vivo")
elif opciones == 2:
 print("Has elegido la puerta negra pequeña")
 print("Este puerta te llevo a un final inesperado")
 print("game over")
elif opciones == 3:
 print("Has elegido la puerta verde esmeralda")
 espada = int(input("Esta puerta te llevo a elegir dos espadas para enfrentar a el dragon, 1: espada de fuego, 2: espada de hielo "))
 if espada == 1:
    print ("haras un daño de 30 puntos al dragon")
    decision = int(input("Ahora debera eleguir si quieress continuar o te retiraras: 1,continuar,2,retirarme "))
    if decision == 1:
        print("sigues vivo")
        print("felicidades has continuado el camino toma una manzana dorada la cual te curara en medio de la batalla")
        print(int("tendras que enfrentartea ,1 ,orco,2,orda de esqueletos"))
        if decision == 1:
            print("te enfrentas a un orco con 200 puntos de vida")
            print(int("que decides: 1;atacar, 2;huir"))
            if decision == 1:
               print ("felicidades has ganado ahora sigue tu camino de recompensa tendras una armadura de hierro")
               print(int("ahora tienes que pasar por una camino de ,1 lodo,2 camino de piedras"))
               if decision == 1:
                   print("pierdes 10 puntos de vida")
                   print(int("ahora deberas enfrentarte al dragon, 1,atacar, 2,huir"))
                   if decision == 1:
                      print("lo siento has muerto debiste eleguir una mejor espada")
                   elif decision == 2:
                      print ("has ganado pero eres un cobarde")
               elif decision == 2:
                   print("pierdes 20 puntos de vida")
        elif decision == 2:
            print("te enfrentas a una horda de esqueletos con 50 puntos de vida cada uno")
    elif decision == 2:
        print("game over")
 elif espada == 2:
    print("haras un daño de 50 puntos al dragon")
    decision = int(input("Ahora debera eleguir si quieress continuar o te retiraras: 1,continuar,2,retirarme "))
    if decision == 1:
        print("sigues vivo")
        print("felicidades has continuado el camino toma una manzana dorada la cual te curara en medio de la batalla")
        print(int("tendras que enfrentartea :1 orco,2,orda de esqueletos"))
        if decision == 1:
            print("te enfrentas a un orco con 200 puntos de vida")
            print(int("que decides: 1;atacar, 2;huir"))
            if decision == 1:
                print ("felicidades has ganado ahora sigue tu camino de recompensa tendras una armadura de hierro")
                print(int("ahora tienes que pasar por una camino de ,1 lodo,2 camino de piedras"))
                if decision == 1:
                    print("pierdes 10 puntos de vida")
                    print(int("ahora deberas enfrentarte al dragon, 1,atacar, 2,huir"))
                    if decision == 1:
                        print("has ganado eres un heroe y todos te adoran en el reino")
                    elif decision == 2:
                        print ("has ganado pero eres un cobarde")
        elif decision == 2:
            print("game over")
    elif decision == 2:
        print("game over")
elif opciones == 4:
   print("Has elegido la puerta de celda")
   print("Detras de esta puerta hay una niebla que no te deja ver")
   decision = int(input("¿Qué decides hacer? 1: avanzar, 2: retroceder "))
   if decision == 1:
       print("Te has adentrado en la niebla")
       print("game over")
   elif decision == 2:
       print("Has regresado a la sala principal")
       print("game over")
   else:
       print("Has muerto")
