numero_secreto = 4
intento =int(input("adivina el numero (entre 1 y 10): "))

while intento != numero_secreto:
    if intento < numero_secreto:
        print("demasiado bajo")
    else:
        print("demasiado alto")
    intento =int(input("intentete de nuevo:"))
print("!correcto el numero era ", numero_secreto)
