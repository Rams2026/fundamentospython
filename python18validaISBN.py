print("valida ISBN")
texto = input()
longitud = len(texto)
for i in range(10):
    letra = int(texto[i])
    #print("Texto[i]", texto[i])
    #print("Posicion[" + str(i) + "]" + letra)
    total = int(texto[i]) * int(letra)
    print("total", total(i))

suma = 0
for i in range(len(isbn)):
    caracter = isbn[i]
    numero = int(caracter)
    multi = numero * (i + 1)
    suma = suma + multi
    