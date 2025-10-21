import random
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

limite_transferencia = 12000

while ejecutar:
    menu_options = ["retirar", "abonar", "transferir", "servicios", "salir"]
    random.shuffle(menu_options)

    print("******Selecciona una opcion******")
    for idx, opt in enumerate(menu_options, start=1):
        if opt == "retirar":
            etiqueta = f"{nombre} La opción es para retirar dinero"
        elif opt == "abonar":
            etiqueta = f"{nombre} La opcion es para abonar dinero"
        elif opt == "transferir":
            etiqueta = f"{nombre} La opcion es para consultar transferir"
        elif opt == "servicios":
            etiqueta = f"{nombre} La opcion es para pagar servicios (agua/luz/internet)"
        elif opt == "salir":
            etiqueta = f"{nombre} La opcion es para salir"
        print(f"{idx}. {etiqueta}")
    print("********************************")

    entrada = input("Ingrese el número de la opción que desea elegir: ")
    try:
        opcion_num = int(entrada)
        if not 1 <= opcion_num <= len(menu_options):
            print("Opción no válida")
            continue
    except ValueError:
        print("Entrada no válida. Ingrese un número.")
        continue

    opcion = menu_options[opcion_num - 1]

    if opcion == "retirar":
        print(nombre + " ha seleccionado la opción de retirar dinero")
        retiro = int(input("cuanto dinero desea retirar?"))
        ahorro = ahorro - retiro
        print("tu nuevo saldo es de", ahorro)

    elif opcion == "abonar":
        print(nombre + " ha seleccionado la opción de abonar")
        abono = int(input("cuanto dinero desea abonar?"))
        ahorro = ahorro + abono
        print("tu nuevo saldo es de", ahorro)

    elif opcion == "transferir":
        print(nombre + " ha seleccionado la opción de transferir ")
        transferencia = int(input("cuanto dinero desea transferir? "))
        if transferencia > limite_transferencia:
            print("La transferencia excede el límite de", limite_transferencia, "pesos. Operación cancelada.")
        elif transferencia > ahorro:
            print("Saldo insuficiente para transferir.")
        else:
            ahorro -= transferencia
            print("Transferencia realizada. Tu nuevo saldo es de", ahorro)

    elif opcion == "servicios":
        print("Seleccione el servicio a pagar:")
        print("1. Agua - 800")
        print("2. Luz - 1200")
        print("3. Internet - 1500")
        print("4. Cancelar")
        servicio = int(input("Ingrese la opción del servicio: "))
        if servicio == 1:
            monto = 800
            nombre_servicio = "Agua"
        elif servicio == 2:
            monto = 1200
            nombre_servicio = "Luz"
        elif servicio == 3:
            monto = 1500
            nombre_servicio = "Internet"
        else:
            print("Pago de servicios cancelado.")
            continue

        if monto > ahorro:
            print("Saldo insuficiente para pagar", nombre_servicio, ". Monto:", monto, "Saldo:", ahorro)
        else:
            ahorro -= monto
            print("Pago de", nombre_servicio, "realizado por", monto, "pesos. Nuevo saldo:", ahorro)

    elif opcion == "salir":
        print("gracias por usar nuestros servicios")
        ejecutar = False

