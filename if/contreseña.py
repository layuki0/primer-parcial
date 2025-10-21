contraseña = 9909
intentos = 3

while intentos > 0:
    intento = int(input("contraseña: "))
    if intento == contraseña:
        print("acceso completo")
        break
    else:
        print("contraseña incorrecta")
        intentos -= 1
        if intentos == 1:
            print("ultimo intento, ¿quieres unas preguntas de seguridad para pasar? 1=si, 2=no")
            if int(input()) == 1:
                print("nombre de mascota?")
                if input() == "firulais":
                    print("correcto")
                    break
                else:
                    print("incorrecto")
                    intentos -= 1
    if intentos == 0:
        print("llamando a la policia")

