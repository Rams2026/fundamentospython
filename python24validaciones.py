import libreria24validaciones
print("Validar ISBN")
print("Introduzca ISBN")
isbn = input()
respuesta = libreria24validaciones.validaIsbn(isbn)
if (respuesta == True):
    print("El ISBN esta BIEN")
else:
    print("El isbn no es correcto")
print("Fin del programa Main") 
