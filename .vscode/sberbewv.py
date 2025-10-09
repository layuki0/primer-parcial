positivos = negativos = ceros = 0
contador = 0
while contador < 5:
    num = int(input("Ingresa numero: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        ceros += 1
    contador += 1
print("positivos" ,positivos)
print("negativos", negativos)
print("ceros:",ceros)
