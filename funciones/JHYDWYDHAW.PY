productos = ["CocaCola", "Pepsi", "Sabritas", "Doritos", "Galletas", "Chicles"]
precios = {
    "CocaCola": 20,
    "Pepsi": 18,
    "Sabritas": 15,
    "Doritos": 17,
    "Galletas": 12,
    "Chicles": 5
}
total = 0

def combo(prod1, prod2):
    if prod1 == "CocaCola" and prod2 == "Sabritas":
        print("Combo CocaCola + Sabritas aplicado (-$5)")
        return 5
    elif prod1 == "Pepsi" and prod2 == "Doritos":
        print("Combo Pepsi + Doritos aplicado (-$4)")
        return 4
    elif prod1 == "Galletas" and prod2 == "CocaCola":
        print("Combo Galletas + CocaCola aplicado (-$3)")
        return 3
    else:
        print("No hay combo disponible")
        return 0

while True:
    print("Este es un oxxo")
    for producto in productos:
        if producto == "CocaCola":
            print(producto + "  $20")
        elif producto == "Pepsi":
            print(producto + "  $18")
        elif producto == "Sabritas":
            print(producto + "  $15")
        elif producto == "Doritos":
            print(producto + "  $17")
        elif producto == "Galletas":
            print(producto + "  $12")
        elif producto == "Chicles":
            print(producto + "  $5")
    compra = input("¿Qué producto deseas comprar? (escribe 'salir' para terminar): ")
    if compra.lower() == 'salir':
        print("Gracias por visitar el oxxo. ¡Hasta luego!")
        print(f"Total a pagar: ${total}")
        break
    elif compra in productos:
        print(f"Has comprado {compra}.")
        total += precios[compra]
        print(f"Subtotal: ${total}")
        usar_combo = input("¿Quieres agregar otro producto para combo? (si/no): ").lower()
        if usar_combo == "si":
            compra2 = input("¿Cuál es el segundo producto?: ")
            if compra2 in productos:
                total += precios[compra2]
                descuento = combo(compra, compra2)
                total -= descuento
                print(f"Subtotal con combo: ${total}")
            else:
                print("Producto no disponible para combo.")
    else:
        print("Producto no disponible.")
