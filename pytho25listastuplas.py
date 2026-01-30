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

"""
lista =[]

while(len(lista) != 5):
    print("dime un nombre")
    nombre = input()
    if nombre in lista:
        print("nombre repetido")
    else:
        lista.append(nombre)

    print(len(lista))
    """
print("Listas con Python")
listaNumeros = [3,5,7,11,2,9,88]
#PODEMOS DIBUJAR DIRECTAMENTE LAS LISTAS
#Podemos ordenar de forma ASCENDENTE
#listaNumeros.sort()
#ORDEN DESCENDENTE
#listaNumeros.sort(reverse=True)
#print(listaNumeros)
#Podemos recorrer todos los elementos del
#conjunto 1 a 1 con un for (Todo empieza en CERO)
for i in range(len(listaNumeros)):
    print(listaNumeros[i])
#Listas pueden ser de cualquier tipo
listaNombres = ["Ana", "Maria", "Adrian", "Lucia", "Diana", "Adrian"]
#Accedemos a los nombres por su índice
print("Nombre[2]: ", listaNombres[2])
print("Nombre[4]: ", listaNombres[4])
#append añade un nuevo elemento al final de la lista
listaNombres.append("El nuevo")
#Podemos insertar un nuevo elemento en una posicion
listaNombres.insert(1, "Infiltrado")
#El metodo remove() elimina el primer elemento que se encuentre
#listaNombres.remove("Adrian")
#Podemos eliminar por indice/posicion
listaNombres.pop(6)
#podemos borrar rangos
del listaNombres[0:2]
#Podemos preguntar por elementos dentro del conjunto
respuesta = "Diana" in listaNombres
print("Diana existe ", respuesta)
#Podemos recorrer cada elemento
for i in range(len(listaNombres)):
    print(listaNombres[i])
#Podemos borrar toda la lista
listaNombres.clear()
print(listaNombres)
print("Tuplas")
#Elementos que son estaticos
tupla = ("Leche", "Cacao", "Avellanas", "Azucar")
print("tupla[1], ", tupla[1])
#La tupla no se puede modificar
#tupla[1] = "Vainilla"
print(tupla)
#Quiero recorrer cada elemento de la tupla
for elem in tupla:
    print(elem)



