import random

while True:

    monstros = {
        "vampiro": ["le teme al sol", "tiene colmillos", "bebe sangre"],
        "zombie": ["camina lento", "busca cerebros", "esta medio podrido"],
        "bruja": ["tiene escoba", "hace pociones", "usa sombrero puntiagudo"],
        "fantasma": ["es blanco", "flota", "atraviesa paredes"],
        "esqueleto": ["no tiene carne", "hace ruido al caminar", "esta en todos los cuerpos"]
    }
    respuestas = { 
        "vampiro": "🧛🏼",
        "zombie": "🧟‍♀️",
        "bruja": "🧙🏻",
        "fantasma": "👻",
        "esqueleto": "🩻",
    }
    monstro = random.choice(list(monstros.keys()))
    pistas = monstros [monstro]
    print("🎃 bienvenido al juego de halloween 🎃")
    print("adivine el mounstro.........\n")

    for i,pista in enumerate (pistas, 1):
        print(pista)


    respuesta = input("\n ¿quien crees que es?").strip().lower()

    if respuesta == monstro:
        print("correcto era un ", monstro)
        break
    else:
        print("era un ",respuesta,"vuelve a intentarlo")
