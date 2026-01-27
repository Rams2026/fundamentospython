def convertirMayusculas(texto):
    return texto.upper()
def convertirMinusculas(texto):
    return texto.lower()
def concatenar(texto1, texto2):
    resultado = texto1 + texto2
    return resultado
def mostrarmenu():
    print("Seleccione una opcion")
    print("1.- Convertir a mayusculas")
    print("2.- Convertir a minusculas")
    print("3.- Concatenar textos")
#PROGRAMA PRINCIPAL MAIN
print ("Ejemplos metodos return")
print("introduce un texto")
valor= input()
mostrarmenu()
opcion =int(input())
resultado =""
if (opcion == 1):
    resultado = convertirMayusculas(valor)
elif (opcion == 2):
    resultado = convertirMinusculas(valor)
elif(opcion == 3):
    print("Dame otro texto")
    otro = input()
    resultado = concatenar(valor, otro)
print(resultado)

print("FIN PGM")




