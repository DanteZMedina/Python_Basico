def palindromo(palabra):
    palabra = palabra.replace(" ", "") #quitamos espacios
    palabra = palabra.lower() #todo en minusculas
    palabra_invertida = palabra[::-1] #pasamos palabra al reves
    if palabra == palabra_invertida: # preguntamos si son iguales
        return True
    else:
        return False


def run():
    palabra = input('Escribre una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es Palindromo")
    else:
        print("No es Palindromo")

#entry point

if __name__ == '__main__':
    run()
