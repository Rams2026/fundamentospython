
import oracledb

connection = oracledb.connect(user="system", password="oracle"
                              , dsn="localhost/FREEPDB1")
cursor = connection.cursor()

print("Introduce el Hospital: ")
Func = int(input())

print("Incremento salarial: ")
IncrSal = int(input())

sql = "update PLANTILLA set SALARIO = SALARIO + :IncrSal where FUNCION=:Func"
#de izquierda a derecha, buscara dentro de la consulta los :
cursor.execute(sql, (IncrSal, Func,))
registros = cursor.rowcount
connection.commit()
print(f"Empleados afectados: {registros}")
sql = "select * from PLANTILLA where HOSPITAL_COD=:inventado"
cursor.execute(sql, (Func,))
for row in cursor:
    print(row)
   # print(f"{row[1]}, Salario: {row[5]}")
cursor.close()
connection.close()
print("Fin de programa")