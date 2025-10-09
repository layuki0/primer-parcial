def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    return sum(1 for char in cadena if char in vocales)

cadena = input("Ingrese un texto:")
print("Número de vocales:", contar_vocales(cadena))