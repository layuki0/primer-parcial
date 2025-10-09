while True:
    def es_palindromo(palabra):
        palabra = palabra.replace(" ", "").lower()
        return palabra == palabra[::-1]

    entrada = input("Ingresa una palabra o frase: ")
    if es_palindromo(entrada):
        print(f'"{entrada}" es un palíndromo.')
    else:
        print(f'"{entrada}" no es un palíndromo.')
