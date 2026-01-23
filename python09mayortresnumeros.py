print("El mayor de los 3 numeros")
print ("Primer numero:")
num1 = int(input())
num2 = int(input("Segundo numero:"))
num3 = int(input("Tercer numero:"))
mayor=0
menor=0
interm=0
#recuperamos el mayor
if(num1 > num2 and num1 > num3):
    mayor = num1
elif (num2 > num1 and num2 > num3):
    mayor  = num2
else:
    mayor = num3
#recuperamos el menor
if(num1 < num2 and num1 < num3):
    menor = num1
else:
    menor =num3
#recuperamos el intermedio
suma = num1 + num2 + num3
interm = suma - mayor- menor
print("Mayor", mayor)
print("Menor", menor)
print("Intermedio", interm)



       


