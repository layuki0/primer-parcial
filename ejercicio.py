opcion = int(input("Escriba la opcion desea usar,¿1 o 2? "))
if opcion == 1:
    print("conversor de numero a palabras")
    opcion_uno = int(input("¿Cual es el numero que desea convertir a palabras?"))
    if opcion_uno == 1:
        print("El numero es uno")
    else:
        print("El numero se desconoce")
elif opcion == 2:
    print("conversor de palabras a numero")
    opcion_dos = input("¿Cual es la palabra que desea convertir a numero?")
    if opcion_dos == "uno":
        print("El numero es uno")
    else:
        print("El numero se desconoce")
else:
    print("opcion no disponible")
