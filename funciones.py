cadena = "hola como estas mi nombre es edgar y tengo 16 años y estoy en lam prepa tengo 5 materias y me gustan los tacos"
vocales = "aeiouAEIOU"
contador =0
for letra in cadena:
    if letra in vocales:
        contador +=1   
print ("numero de vocales:",contador)
