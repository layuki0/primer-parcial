print("Bienvenido a BBVA")
ejecutar = True

nip = 2435
intentos = 3

while ejecutar:
    nip = int(input("ingrese su nip: "))
    if nip == 2435:
        print("nip correcto")
        break  
    else:
        intentos -= 1
        print("nip incorrecto intentos restantes", intentos)
else:
    print("acceso denegado")
        


nombre = input("¿Cual es tu nombre ?")
ahorro = int(input("¿Cuanto dinero tienes ahorrado ?"))
print("Hola", nombre, "tienes", ahorro, "pesos en tu cuenta.")

while ejecutar:
    print("******Seleciona una opcion******")
    print(nombre + " La opción es para retirar dinero , 1")
    print(nombre + " La opcion es para abonar dinero , 2")
    print(nombre + " La opcion es para consultar saldo , 3")
    print(nombre + " La opcion es para salir , 4")
    print("********************************")

    opcion = int(input(" que opcion deseas elegir?"))

    if opcion == 1:
        print(nombre + " ha seleccionado la opción 1")
        retiro = int(input("cuanto dinero desea retirar?"))
        ahorro = ahorro - retiro
        print("tu nuevo saldo es de", ahorro)
        
    elif opcion == 2:
        print(nombre + " ha seleccionado la opción 2")
        abono = int(input("cuanto dinero desea abonar?"))
        ahorro = ahorro + abono
        print("tu nuevo saldo es de", ahorro)
    elif opcion == 3:
        print(nombre + " ha seleccionado la opción 3")
        print("tu saldo actual es de", ahorro)
    elif opcion == 4:
        print("gracias por usar nuestros servicios")
        ejecutar = False
        print("Opción no válida")
