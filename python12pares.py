print("RANGO DE NUMEROS con For")
inicial =6
numero_final =20
for i in range (inicial, numero_final + 1):
    if(i % 2 == 0):
        print(i)


print("RANGO DE NUMEROS con WHILE")
while (inicial <= numero_final):
    if (inicial % 2 == 0):
        print(inicial)
        inicial = inicial + 1
print("fin de programa")