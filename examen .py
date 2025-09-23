print("Este es la aerolínea de Aeroméxico")
print("¿A donde desea viajar?")
print("Alemania")
print("Francia")
print("Italia")
print("Japón")
lugar = str(input())

clase = input("que clase de viaje desea viajar?(primera clase,clase economica)")
if clase == "primera clase":
    print("El costo del viaje a Alemania en primera clase es de $500")
    total = 500
    print(str("Desea llevar equipaje extra (1) si (2) no "))
    if input("") == 1:
            print ("tendra un descuento especial del 15% por llevar equipaje extra")
            total += 50
            print("El costo total de su viaje es de $", total)
            print("Disfrute su viaje")
    elif input("") == 2:
            print("El costo total de su viaje es de $", total)
            print("Disfrute su viaje")
elif clase == "clase economica":
        print("El costo del viaje a Alemania en clase economica es de $250")
        total = 250
        print(str("Desea llevar equipaje extra (1) si (2) no "))
        if input("Muy bien") == 1:
            total +=50
            print("El costo total de su viaje es de $", total)
            print("Disfrute su viaje")
        elif input("Muy bien") == 2:
            print("El costo total de su viaje es de $", total)
            print("Disfrute su viaje")

print("su lugar de destino es ", lugar , "y su clase de viaje es ", clase ,"con un costo total de $", total)