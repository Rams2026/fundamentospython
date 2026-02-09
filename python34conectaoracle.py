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
row = cursor.fetchone() #primera fila
print("Fila: ", row)
row = cursor.fetchone() #segunda fila
print("Fila: ", row)
row = cursor.fetchone() #tercera fila
print("Fila: ", row)
row = cursor.fetchone() #cuarta fila
print("Fila: ", row)
row = cursor.fetchone() #un none(null en BBDD)
print("Fila: ", row)

""" Siempre que finalicemos las acciones debemos liberar los recursos """
cursor.close()
connection.close()
print("Fin del pgm")