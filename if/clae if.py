traductor = "Bienvenido al traductor de idiomas"
idioma = input("¿Qué idioma desea traducir? (japonés, alemán, ruso) ")
ejecutar = True
print(traductor)
print(idioma)
while ejecutar:
	if idioma == "japones":
		print("Has seleccionado japones.")
		print("¿Qué palabra desea traducir? (hola, adiós, por favor, gracias,gato,perro,agua,fuego,tierra,aire,tortuga,pez,ave,mar,sol)")
		palabra = input()
		if palabra == "hola":
			print("こんにちは (Konnichiwa)")
		elif palabra == "adiós":
			print("さようなら (Sayōnara)")
		elif palabra == "por favor":
			print("お願いします (Onegaishimasu)")
		elif palabra == "gracias":
			print("ありがとうございます (Arigatō gozaimasu)")
		elif palabra == "gato":
			print("猫 (Neko)")
		elif palabra == "fuego":
			print("火 (Hi)")
		elif palabra == "tierra":
			print("土 (Tsuchi)")
		elif palabra == "aire":
			print("空気 (Kūki)")
		elif palabra == "tortuga":
			print("亀 (Kame)")
		elif palabra == "pez":
			print("魚 (Sakana)")
		elif palabra == "ave":
			print("鳥 (Tori)")
		elif palabra == "mar":
			print("海 (Umi)")
		elif palabra == "sol":
			print("太陽 (Taiyō)")
		break
	elif idioma == "aleman":
		print("Has seleccionado alemán.")
		print("¿Qué palabra desea traducir? (hola, adiós, por favor, gracias,gato,perro,agua,fuego,tierra,aire,tortuga,pez,ave,mar,sol)")
		palabra = input()
		if palabra == "hola":
			print("Hallo")
		elif palabra == "adiós":
			print("Auf Wiedersehen")
		elif palabra == "por favor":
			print("Bitte")
		elif palabra == "gracias":
			print("Danke")
		elif palabra == "gato":
			print("Katze")
		elif palabra == "perro":
			print("Hund")
		elif palabra == "agua":
			print("Wasser")
		elif palabra == "fuego":
			print("Feuer")
		elif palabra == "tierra":
			print("Erde")
		elif palabra == "aire":
			print("Luft")
		elif palabra == "tortuga":
			print("Schildkröte")
		elif palabra == "pez":
			print("Fisch")
		elif palabra == "ave":
			print("Vogel")
		elif palabra == "mar":
			print("Meer")
		elif palabra == "sol":
			print("Sonne")
		else:
			print("Palabra no reconocida")
			break
		break
	elif idioma == "ruso":
		print("Has seleccionado ruso.")
		print("¿Qué palabra desea traducir? (hola, adiós, por favor, gracias,gato,perro,agua,fuego,tierra,aire,tortuga,pez,ave,mar,sol)")
		palabra = input()
		if palabra == "hola":
			print("Привет (Privet)")  
		elif palabra == "adiós":
			print("До свидания (Do svidaniya)")
		elif palabra == "por favor":  
			print("Пожалуйста (Pozhaluysta)")
		elif palabra == "gracias":
			print("Спасибо (Spasibo)")
		elif palabra == "gato":
			print("Кошка (Koshka)")
		elif palabra == "perro":
			print("Собака (Sobaka)")
		elif palabra == "agua":
			print("Вода (Voda)")
		elif palabra == "fuego":
			print("Огонь (Ogon')")
		elif palabra == "tierra":
			print("Земля (Zemlya)")
		elif palabra == "aire": 
			print("Воздух (Vozdukh)")
		elif palabra == "tortuga":  
			print("Черепаха (Cherepakha)")
		elif palabra == "pez":
			print("Рыба (Ryba)")
		elif palabra == "ave":  
			print("Птица (Ptitsa)")
		elif palabra == "mar":
			print("Море (More)")
		elif palabra == "sol":
			print("Солнце (Solntse)")
		else:
			print("Palabra no reconocida")
			break
		break
	else:
		print("Idioma no reconocido")
print("Gracias por usar el traductor")