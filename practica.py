idioma = str(input("¿a que idioma quiere traducir?(español o ingles)"))
if idioma == "español":
    opcion = input("que palabra desea traducir?(blue o red) ")
    if opcion == "blue":
        print("El color es azul")
        if opcion == "blue":
            print("se creó al ser producido como el primer pigmento sintético por los antiguos egipcios alrededor del 2200 a.C.")
    elif opcion == "red":
        print("El color es rojo")
        if opcion == "red":
            print("fuentes naturales diversas y fue uno de los primeros colores utilizados por los humanos, obteniéndose de la arcilla ocre para pintura corporal y rupestre en la prehistoria")
    else:
        print("opcion no disponible")
elif idioma == "ingles":
    opcion_dos = str(input("que color desea traducir?(azul o rojo)"))
    if opcion_dos == "azul":
        print("The color is blue")
        if opcion_dos == "azul":
            print("beginning with precious lapis lazuli for jewelry and religious art in ancient Egypt and the Middle East, followed by the invention of the first synthetic pigment, Egyptian blue, and later ultramarine made from lapis in the Renaissance")
    elif opcion_dos == "rojo":
        print("The color is red")
        if opcion_dos== "rojo":
            print("beginning with its use in prehistoric cave paintings from the Paleolithic era and continuing through ancient civilizations, where it was associated with power, warfare, and ceremony")
    else:
        print("opcion no disponible")