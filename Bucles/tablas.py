
def multiplicador(tabla, opcion):
    print("    Seleccionaste la tabla del: " + str(tabla))
    for i in range (11):
        print("    "+str(tabla) + " X " + str(i) + " = " + str(opcion * i))



def run():
    menu = """
    Bienvenido a nuestro menu de tablas 
    Seleccione la tabla que necesita:

    1 - tabla del 1
    2 - tabla del 2
    3 - tabla del 3
    4 - tabla del 4
    5 - tabla del 5
    6 - tabla del 6
    7 - tabla del 7
    8 - tabla del 8
    9 - tabla del 9
    10 - tabla del 10

    Elige una opcion: 
    """
    opcion = int(input(menu))

    if opcion == 1:
        multiplicador(1, opcion)
    elif opcion == 2:
        multiplicador(2, opcion)
    elif opcion == 3:
        multiplicador(3, opcion)
    elif opcion == 4:
        multiplicador(4, opcion)
    elif opcion == 5:
        multiplicador(5, opcion)
    elif opcion == 6:
        multiplicador(6, opcion)
    elif opcion == 7:
        multiplicador(7, opcion)
    elif opcion == 8:
        multiplicador(8, opcion)
    elif opcion == 9:
        multiplicador(9,3875)
    elif opcion == 10:
        multiplicador(10,3875)
    else: 
        print("ingresa una opcion correcta")



if __name__ == '__main__':
    run()