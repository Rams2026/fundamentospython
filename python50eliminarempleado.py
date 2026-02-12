from oracle50empleados import OracleEmpleado

print("Programa eliminar empleado")
#Creamos nuestra clase de Oracle
oracle = OracleEmpleado()
print("Introduzca una empleado")
dato = int(input())
registros = oracle.eliminarEmpleado(dato)
print(f"Empleados eliminados: {registros}")
print("Fin de programa")