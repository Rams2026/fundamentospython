import oracledb
print ("")
print ("Conectando a oracle...")
""" Tenemos un objeto connection que nos pedirá
(user, password, server)   """

connection = oracledb.connect(user="system"
                              , password="oracle"
                              , dsn="localhost/FREEPDB1")


"""Creamos nuestra consulta SQL con los departamentos
la consulta sql desde Python no finaliza en ; """

sql = "select * from DEPT"

""" Creamos un cursor para la consulta"""
cursor = connection.cursor()

"""Debemos ejecutar la consulta para que nos devuelta los datos de Oracle"""
cursor.execute(sql)

"""Aqui ya estan los datos
Una vez qye tenemos  el cursor, debemos leer los datos
Tenemos un metodo llamado fetchone() que se mueve una fila
cada vez que lo ejecutamos
Nos devuelve la fila en que estamos posicionados"""

"""Para comentar en bloque:
   >> Comentar: Command /control + k + u
   
   """
"""row = cursor.fetchone() #primera fila
print("Fila: ", row)
row = cursor.fetchone() #segunda fila
print("Fila: ", row)
row = cursor.fetchone() #tercera fila
print("Fila: ", row)
row = cursor.fetchone() #cuarta fila
print("Fila: ", row)
row = cursor.fetchone() #un none(null en BBDD)
print("Fila: ", row). """

#1) Recorrer el cursor con WHILE
"""row = cursor.fetchone()
while (row != None):
    print("Leer filas...",row)
    row = cursor.fetchone(). """

for numero, nombre, localidad in cursor:
    print(numero, nombre, localidad)
    

""" Siempre que finalicemos las acciones debemos liberar los recursos """
cursor.close()
connection.close()
print("Fin del pgm")