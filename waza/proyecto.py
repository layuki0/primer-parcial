import random
deportes = ["gimnasia", "tennis", "box"]
print("Elige un deporte: gimnasia, tennis, box")
eleccion = input("Seleccione: ").strip().lower()
while True:
    if eleccion == "gimnasia":
        k = ["historia", "deportistas", "juegos recientes", "apuestas"]
        print("¿Qué quieres conocer de la gimnasia? historia, deportistas, juegos recientes, apuestas")
        l = input("Seleccione: ").strip().lower()
        if l == "historia":
            print("La gimnasia tiene sus orígenes en la antigua Grecia se practicaba para desarrollar fuerza, agilidad y belleza corporal, especialmente entre los soldados. Con el tiempo, esta disciplina evolucionó y se convirtió en parte de la educación física. En el siglo XIX, Alemania y Suecia crearon sistemas de entrenamiento estructurados con aparatos como barras y caballos. La gimnasia moderna, tal como se conoce hoy, se consolidó en el siglo XX con la fundación de la Federación Internacional de Gimnasia (FIG) y su inclusión en los Juegos Olímpicos, convirtiéndose en un deporte que combina fuerza, flexibilidad,técnicayarte.")
        elif l == "deportistas":
            p = ["Simone Biles", "Nadia Comaneci", "Larisa Latynina"]
            print("Simone Biles, Nadia Comaneci,Larisa Latynina")
            deportista =(input("Escoga a su deportista")).capitalize()
            if deportista == "Simon Biles":
                print(" La gimnasta más condecorada de la historia; revolucionó la dificultad y el control mental en el deporte.")
            elif deportista == "Nadia Comaneci":
                print(" Primera en lograr un *10 perfecto* en Juegos Olímpicos (1976).")
            elif deportista == "Larisa Latynina":
                print("Dominó la gimnasia olímpica durante los 50s-60s; récord de medallas durante décadas.")
            else:
                print("no hay")
        elif l == "juegos recientes":
            print("El juego importante más reciente se ha llevado a cabo en París 2024, donde Simon Biles gana la medalla de oro, rebeca andrade la de plata y sunisa lee la de bronce.")
        elif l == "apuestas":
            print("gracias y bienvenido a nuestro servicio de apuestas")
            deal = int(input("¿Cuánto dinero va a apostar el día de hoy?: ").strip())
            if deal < 1000:
                print("Gracias pero requerirá cumplir el mínimo de 1000.")
                print("🎰 Bienvenido al sistema de apuestas 🎰")
            elif deal > 1000:
                print ("bienbenido")
                dinero = deal
                opciones = ["Simon", "Kohei"]

                while dinero > 0:
                    print(f"\nTienes {dinero} monedas.")
                    print("Equipos en competencia:", opciones)

                    
                    eleccion = input("¿A quién le apuestas? (simon, kohei o 'salir'): ").capitalize()
                    if eleccion == "Salir":
                        print("Gracias por jugar. ¡Vuelve pronto!")
                        break

                    elif eleccion not in opciones:
                        print("Opción inválida, intenta de nuevo.")
                        continue

                    
                    apuesta = int(input("¿Cuánto deseas apostar?: "))
                    if apuesta > dinero or apuesta <= 0:
                        print("Cantidad no válida.")
                        continue

                    
                    ganador = random.choice(opciones)
                    print(f"🏁 El ganador fue: {ganador}")

                
                    if eleccion == ganador:
                        dinero += apuesta
                        print(f"¡Ganaste {apuesta} monedas! 🎉")
                    else:
                        dinero -= apuesta
                        print(f"Perdiste {apuesta} monedas 💸")

                    if dinero <= 0:
                        print("Te has quedado sin dinero. Fin del juego.")
                    else:
                        print("Muchas gracias por usar el servicio de apuestas.")
                            

            break
    if eleccion == "tenis":
        k = ["historia", "deportistas", "juegos recientes", "apuestas"]
        print("¿Qué quieres conocer del tenis? historia, deportistas, juegos recientes, apuestas")
        l = input("Seleccione: ").strip().lower()
        if l == "historia":
            print("El tenis moderno se originó en Inglaterra durante el siglo XIX, aunque tiene raíces más antiguas en juegos franceses como el 'jeu de paume'. Se popularizó rápidamente y en 1877 se celebró el primer torneo de Wimbledon. Hoy es un deporte global con torneos emblemáticos como los Grand Slam: Wimbledon, Roland Garros, US Open y el Abierto de Australia.")
        elif l == "deportistas":
            p = ["Roger Federer", "Rafael Nadal", "Novak Djokovic"]
            print("Roger Federer, Rafael Nadal, Novak Djokovic")
            deportista = (input("Escoga a su deportista")).capitalize()
            if deportista == "Roger federer":
                print("Considerado uno de los más grandes del tenis, con elegancia, técnica y 20 títulos de Grand Slam.")
            elif deportista == "Rafael nadal":
                print("Conocido como el 'Rey de la Tierra Batida', ha ganado 22 Grand Slams y es símbolo de esfuerzo y constancia.")
            elif deportista == "Novak djokovic":
                print("Destacado por su fortaleza mental y física, es el tenista con más títulos de Grand Slam en la historia.")
            else:
                print("no hay")
        elif l == "juegos recientes":
            print("El torneo más reciente fue el US Open 2024, donde Novak Djokovic se coronó campeón tras una final intensa contra Carlos Alcaraz.")
        elif l == "apuestas":
            print("gracias y bienvenido a nuestro servicio de apuestas")
            deal = int(input("¿Cuánto dinero va a apostar el día de hoy?: ").strip())
            if deal < 1000:
                print("Gracias pero requerirá cumplir el mínimo de 1000.")
                print("🎰 Bienvenido al sistema de apuestas 🎰")
            elif deal > 1000:
                print("bienbenido")
                dinero = deal
                opciones = ["Djokovic", "Alcaraz"]

                while dinero > 0:
                    print(f"\nTienes {dinero} monedas.")
                    print("Jugadores en competencia:", opciones)

                    eleccion = input("¿A quién le apuestas? (djokovic, alcaraz o 'salir'): ").capitalize()
                    if eleccion == "Salir":
                        print("Gracias por jugar. ¡Vuelve pronto!")
                        break

                    elif eleccion not in opciones:
                        print("Opción inválida, intenta de nuevo.")
                        continue

                    apuesta = int(input("¿Cuánto deseas apostar?: "))
                    if apuesta > dinero or apuesta <= 0:
                        print("Cantidad no válida.")
                        continue

                    ganador = random.choice(opciones)
                    print(f"🏁 El ganador fue: {ganador}")

                    if eleccion == ganador:
                        dinero += apuesta
                        print(f"¡Ganaste {apuesta} monedas! 🎉")
                    else:
                        dinero -= apuesta
                        print(f"Perdiste {apuesta} monedas 💸")

                    if dinero <= 0:
                        print("Te has quedado sin dinero. Fin del juego.")
                    else:
                        print("Muchas gracias por usar el servicio de apuestas.")
            
            break
    elif eleccion == "box":
        k = ["historia", "deportistas", "peleas recientes", "apuestas"]
        print("¿Qué quieres conocer del box? historia, deportistas, peleas recientes, apuestas")
        l = input("Seleccione: ").strip().lower()
        if l == "historia":
            print("El boxeo tiene raíces en la antigua Grecia y Roma, pero su forma moderna surgió en Inglaterra durante el siglo XVIII. Con las Reglas de Queensberry en 1867, se introdujeron los guantes y los asaltos. Hoy es un deporte global, símbolo de fuerza, estrategia y superación personal.")
        elif l == "deportistas":
            p = ["Muhammad Ali", "Mike Tyson", "Canelo Álvarez"]
            print("Muhammad Ali, Mike Tyson, Canelo Álvarez")
            deportista = (input("Escoga a su deportista")).capitalize()
            if deportista == "Muhammad ali":
                print("Considerado el más grande, famoso por su técnica, velocidad y activismo fuera del ring.")
            elif deportista == "Mike tyson":
                print("El campeón más joven en la historia de los pesos pesados; su fuerza e intensidad marcaron una era.")
            elif deportista == "Canelo álvarez":
                print("El boxeador mexicano más exitoso de la actualidad, campeón en múltiples categorías de peso.")
            else:
                print("no hay")
        elif l == "peleas recientes":
            print("La pelea más destacada de 2024 fue entre Canelo Álvarez y David Benavídez, donde Canelo retuvo su título unificado por decisión unánime.")
        elif l == "apuestas":
            print("gracias y bienvenido a nuestro servicio de apuestas")
            deal = int(input("¿Cuánto dinero va a apostar el día de hoy?: ").strip())
            if deal < 1000:
                print("Gracias pero requerirá cumplir el mínimo de 1000.")
                print("🎰 Bienvenido al sistema de apuestas 🎰")
            elif deal > 1000:
                print("bienbenido")
                dinero = deal
                opciones = ["Canelo", "Benavidez"]

                while dinero > 0:
                    print(f"\nTienes {dinero} monedas.")
                    print("Boxeadores en competencia:", opciones)

                    eleccion = input("¿A quién le apuestas? (canelo, benavidez o 'salir'): ").capitalize()
                    if eleccion == "Salir":
                        print("Gracias por jugar. ¡Vuelve pronto!")
                        break

                    elif eleccion not in opciones:
                        print("Opción inválida, intenta de nuevo.")
                        continue

                    apuesta = int(input("¿Cuánto deseas apostar?: "))
                    if apuesta > dinero or apuesta <= 0:
                        print("Cantidad no válida.")
                        continue

                    ganador = random.choice(opciones)
                    print(f"🥊 El ganador fue: {ganador}")

                    if eleccion == ganador:
                        dinero += apuesta
                        print(f"¡Ganaste {apuesta} monedas! 🎉")
                    else:
                        dinero -= apuesta
                        print(f"Perdiste {apuesta} monedas 💸")

                    if dinero <= 0:
                        print("Te has quedado sin dinero. Fin del juego.")
                    else:
                        print("Muchas gracias por usar el servicio de apuestas.")
                                

            
            break
        else:
            print("Deporte no válido. Intenta de nuevo.")
            eleccion = input("Seleccione: ").strip().lower()







