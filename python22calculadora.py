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

#PROGRAMA PRINCIPAL MAIN
print ("")
print("Teclea valor1")
valor1= int(input())
print("Teclea valor2")
valor2= int(input())

opcion = -1
while (opcion != 0):

    mostrarmenu()
    opcion =int(input())
    resultado =""
    if(opcion == 1):
        resultado = sumar(valor1, valor2)
        print(resultado)
    elif(opcion == 2):
        resultado = restar(valor1, valor2)
        print(resultado)
    elif(opcion == 3):
        resultado = multiplicar(valor1, valor2)
        print(resultado)
print("FIN PGM")










