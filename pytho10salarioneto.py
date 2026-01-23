print("Calcula el salario neto")

HRS_SEMANALES = int(input("INTRODUZCA HORAS SEMANALES:"))
IMP_POR_HR = input("INTRODUZCA IMPORTE HORA:")
NUM_KMS = int(input("INTRODUZCA KILOMETROS: "))


if(NUM_KMS >= 101 and NUM_KMS <= 900):
    print("NACIONAL", NUM_KMS)
elif (NUM_KMS > 900):
    print("INTERNACIONAL", NUM_KMS)
elif (NUM_KMS < 101):
    print("PROVINCIAL", NUM_KMS) 

SALARIO = int(HRS_SEMANALES * IMP_POR_HR)
print("SALARIO", SALARIO)




