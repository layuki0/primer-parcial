print("Bienvenido a cinepolis")
print("**********************")
refresco = 80
palomitas = 92
nachos = 85
ice = 95
print("Va a ver la pelicula de Spiderman No Way home")
lom=(int(input("desea ordenar un combo (si)(1) (no)(2)")))
While = True
if lom==2:
        print("disfrute la pelicula")
        False
elif lom ==1:
    print("Estos son los combos que tenemos")
    print("Combo ice con skinkles(1) el costo es de $314 pesos")
    print("Combo Nachos(2) el costo es de $242 pesos")
    print("Combo micha(3)el costo es de $324 pesos")
    combo = int(input("¿Qué combo desea ordenar?(1)(2)(3) "))
    if combo == 1:
        print("Ordenaste el combo ice con skinkles, el costo es de $314 pesos")
        total = 314
        agregar = int(input("desea agragar algo mas a su combo, (si)(1),(no)(2)"))
        if agregar == 2:
            print("su total es de $", total)
            print("disfrute la pelicula")
            False
        elif agregar == 1:
                print("¿Que producto va a agregar(refresco,palomitas,nachos,ice)?")
                producto = input()
                if producto == "refresco":
                    total += refresco
                elif producto == "palomitas":
                    total += palomitas
                elif producto == "nachos":
                    total += nachos
                elif producto == "ice":
                    total += ice
                else:
                    print("Producto no valido")
                print("su total es de $", total)
                print("disfrute la pelicula")
                False


        False
    elif combo == 2:
            print("Ordenaste el combo Nachos, el costo es de $242 pesos")
            total = 242
            agregar = int(input("desea agragar algo mas a su combo, (si)(1),(no)(2)"))
            if agregar == 2:
                print("su total es de $", total)
                print("disfrute la pelicula")
                False
            elif agregar == 1:
                print("¿Que producto va a agregar(refresco,palomitas,nachos,ice)?")
                producto = input()
                if producto == "refresco":
                    total += refresco
                elif producto == "palomitas":
                    total += palomitas
                elif producto == "nachos":
                    total += nachos
                elif producto == "ice":
                    total += ice
                else:
                    print("Producto no valido")
                print("su total es de $", total)
                print("disfrute la pelicula")
                False

            False
    elif combo == 3:
            print("Ordenaste el combo micha, el costo es de $324 pesos")
            total = 324
            agregar = int(input("desea agragar algo mas a su combo, (si)(1),(no)(2)"))
            if agregar == 2:
                print("su total es de $", total)
                print("disfrute la pelicula")
                False
            elif agregar == 1:
                print("¿Que producto va a agregar(refresco,palomitas,nachos,ice)?")
                producto = input()
                if producto == "refresco":
                    total += refresco
                elif producto == "palomitas":
                    total += palomitas
                elif producto == "nachos":
                    total += nachos
                elif producto == "ice":
                    total += ice
                else:
                    print("Producto no valido")
                print("su total es de $", total)
                print("disfrute la pelicula")
                False

            False
else:
        print("Opcion no valida, por favor intente de nuevo")
        False
False
