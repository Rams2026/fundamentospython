"""Debemos buscar un ENFERMO por su inscripcion, pediremos la inscripcion al usuario
 y si existe dibujamos sus datos (apellido y direccion) y si no, indicamos que el enfermo
 no existe"""

import oracledb
#conexion a oracle
connection = oracledb.connect(user="SYSTEM", password="oracle", dsn="localhost/FREEPDB1")
print("conectado")
print("\n")
print("Introduce la Inscripcion:")

numInscripcion = input()
## Hacemos una consulta para buscar al enfermo
sql = "select * from ENFERMO where inscripcion =" + numInscripcion
##print(sql)

# Creamos un cursor
cursor = connection.cursor()

# Ejecutamos la consulta para traer los datos
cursor.execute(sql)

# recuperamos la primera fila
row = cursor.fetchone()

# Comprobamos si tenemos datos o no en la fila
if(row == None):
    print("No existe el enfermo...")
else:
    #Recuperamos los datos
    apellido = row[1] #APELLIDO
    direccion = row[2]#DIRECCION
    print("NOMBRE: " + apellido)
    print("DIRECCION: " + direccion)

#Liberamos los recursos
cursor.close()
connection.close()
print("\nFIN DE PGM")
