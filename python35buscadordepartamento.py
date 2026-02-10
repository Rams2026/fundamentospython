"""Buscar un departamento por su ID"""
import oracledb
#conexion a oracle
connection = oracledb.connect(user="SYSTEM", password="oracle", dsn="localhost/FREEPDB1")
print("conectado")
print("")
print("Introduce un ID de departamento")
iddepartamento = input()

# Hacemos una consulta para buscar un departamento
sql = "select * from DEPT where DEPT_NO=" + iddepartamento
print(sql)

# Creamos un cursor
cursor = connection.cursor()

# Ejecutamos la consulta para traer los datos
cursor.execute(sql)

# recuperamos la primera fila
row = cursor.fetchone()

# Comprobamos si tenemos datos o no en la fila
if(row == None):
    print("No existe el departamento")
else:
    #Recuperamos los datos
    nombre = row[1] #DNOMBRE
    localidad = row[2] #LOCALIDAD
    print(nombre + "," + localidad)

#Liberamos los recursos
cursor.close()
connection.close()
print(" ")
print("FIN DE PGM")







