def sumar(n1,n2):
    return n1 + n2

def restar(n1,n2):
    return n1 - n2

def multiplicar(n1,n2):
    return n1 * n2

def mostrarmenu():
    print("Seleccione una opcion")
    print("0.- EXIT")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")

def getNumero():
    print("Introduzca un numero")
    aux = input()

    while(aux.isdigit()== False):
        print("No es numero")
        print("introduzca un numero")
        aux = int()
        num = int(aux)
        return num
