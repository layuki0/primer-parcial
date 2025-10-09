def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma
numeros = []
contador =0

cantidad = int (input("cuantos numeros quieres sumar"))
while contador < cantidad:
    entrada =int(input(f"ingrese el numero{contador +1 }:"))
    numeros.append(entrada)
    contador +=1
resultado = sumar_lista(numeros)
print("la suma total:",resultado)