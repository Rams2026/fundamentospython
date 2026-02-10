"""xxx"""

import oracledb
#conexion a oracle
connection = oracledb.connect(user="SYSTEM", password="oracle", dsn="localhost/FREEPDB1")
print("conectado")
print("\n")
print("Introduce el turno(T,M,N):")

turno = input()
## Hacemos una consulta para buscar al enfermo
sql = "select apellido, funcion from PLANTILLA where turno ='" + turno +"'"
print(sql)

# Creamos un cursor
cursor = connection.cursor()

# Ejecutamos la consulta para traer los datos
cursor.execute(sql)

# recuperamos la primera fila
row = cursor.fetchone()

# Comprobamos si tenemos datos o no en la fila

for row in cursor:
    apellido =row[0]
    funcion = row[1]
    print(apellido + ","+funcion )

#Liberamos los recursos
cursor.close()
connection.close()
print("\nFIN DE PGM")
