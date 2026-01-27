print("Ejemplos clase String")
texto = "primero pYton"

print("upper", texto.upper())
print("lower", texto.lower())
print("replace", texto.replace("o","@"))
print("letra 0", texto[0])
print("longitud", len(texto))
print("find(p)", texto.find("p"))
print("find(z)", texto.find("z"))
#SOBRECARGA DE UN METODO
print("find(p,index):", texto.rfind("p"))
print("rfind(p)")
print("startswtih(a)", texto.isdigit())
print("isdigit()", texto.isalpha())
print("isalnum", texto.isalnum())

subcadena = texto[2: 5]
print("texto`[2: 5]", subcadena)
#PODEMOS RECORRER CADA CARACTER CON UN BUCLE
longitud = len(texto)
for i in range(13):
    letra = texto[i]
    print("letra[" + str(i) + "]" + letra)
