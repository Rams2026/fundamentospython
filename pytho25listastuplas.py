"""
print ("Listas con python")

listaNumeros = [3, 5, 7, 11, 2, 9, 88]
# imprimir las listas
print(listaNumeros)
# ordenar la lista
listaNumeros.sort(reverse=False)
print(listaNumeros)
# Recorrer todos los elementos del conjunto 1a1 con un for(todo empieza en cero)
for i in range(len(listaNumeros)):
    print(listaNumeros[i])

"""
"""
nombre =input("introduce tu nombre:")
veces =int(input("introduce el numero de correos: "))

for i in range(veces):
    print(f"{nombre}{i+1}@gmail.com")

"""
"""
provincias = dict()
provincias = {
    111 : "AAAA", 
    222 : "BBBB", 
    333 : "CCCC"
    }
# provincias.clear()
# print(provincias.get(222))
for clave, valor in provincias.items():
    print("key " + str(clave) + ", value: " + valor)
print("==============")
print(provincias)
print("==============")
for clave in provincias.keys():
    print(clave)
print("==============")
for valor in provincias.values():
    print(valor)
print("==============")
provincias.setdefault(223, "BBB")
"""
tupla = ("Leche", "cacao", "azucar")

"""
for i in range(len(tupla)):
    elemento = tupla[i]
    #print(tupla[i])
    print(f"{i+1}.- {elemento}")


for i in range(len(tupla)):
    elemento = tupla[i]
    #print(tupla[i])
    print(f"{i+1}.- {elemento}")
"""
"""

listaNombres = input("teclea los nombres: ").split(',')
nombres = tuple(listaNombres)
print(nombres)
"""
Lista =[]


while(len(lista) ¡= 5):
    print("dime un nombre")
    nombre = input()
    if (nombre in lista):
        print("nombre repetido")
    else
        lista.append(nombre)
print(n)



