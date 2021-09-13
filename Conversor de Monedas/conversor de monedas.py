
menu = """
Bienvenido al conversor de monedas 👌👌

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: 
"""

def conversion(tipo_pesos, valor_dolar):
    pesos = float(input ("Ingrese los pesos " + tipo_pesos +  " a cambiar: \n"))
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str (dolares)
    print("Tienes $" + dolares + " dolares")

opcion = int(input(menu))

if opcion == 1:
    conversion("Colombianos",3875)
elif opcion == 2:
    conversion("Argentinos", 97.48)
elif opcion == 3:
    conversion("Mexicanos", 20.35)
else: 
    print("ingresa una opcion correcta")


# pesos = float(input ("Ingrese los pesos colombianos a cambiar: \n"))
# valor_dolar = 3875
# dolares = pesos / valor_dolar
# dolares = round(dolares, 2)
# dolares = str (dolares)
# print ("Tienes $" + dolares + " dolares" )

# pesosMexicanos = float(input("Ingresa la cantidad de pesos que quieres cambiar: \n"))
# dolar_hoy = 20.18
# cambio = pesosMexicanos / dolar_hoy
# cambio = round(cambio, 2)
# cambio = str(cambio)
# print("Tienes: $ " + cambio + " dolares")

# dolarin = float(input("Cuantos dolares quieres cambiar: \n"))
# regalias = 20.19
# comodin = dolarin * regalias
# comodin = round (comodin, 2)
# comodin = str (comodin)
# print("Te alcanza para todo y tienes: $" + comodin + " chingo de pesos")
