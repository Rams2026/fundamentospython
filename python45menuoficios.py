import oracledb

connection = oracledb.connect(user="SYSTEM", password="oracle"
                              , dsn="localhost/FREEPDB1")
cursor = connection.cursor()


""" inicio ejemplo 1

#Generamos una lista de oficios vacia[]
listaOficios = []
#Agregamos datos a la lista con Append
listaOficios.append("Analista")
listaOficios.append("Director")
listaOficios.append("Programador")
listaOficios.append("Vendedor")
listaOficios.append("Becario")

#Recorremos la lista para el menu
contador = 1
for ofi in listaOficios:
    #agregamos un contador para que imprima la secuencia de numeros
    print(f"{contador}.- {ofi}")
    contador = contador + 1
# Capturamos el numero seleccionado

print(f"Selecciona una Opcion: ")
opcion =int(input())
oficioSeleccionado = listaOficios[opcion - 1] #obtiene el oficio por su posicion
print(f"Opcion seleccionada: {oficioSeleccionado} ")
#Consultamos los empleados con el oficio seleccionado
sql="select * from EMP where OFICIO =:oficio"
cursor.execute(sql, (oficioSeleccionado,))

print(" -----Lista de empleados-----")

for row in cursor:
    print(f"- {row[1]}")

cursor.close()
connection.close() 

print("Fin de Pgm")

fin ejemplo 1""" 


#Generamos una lista de oficios vacia[]
listaOficios = []

#Recuperamos de la BBDD los oficios
sql = "select distinct OFICIO from EMP"
cursor.execute(sql)

#Recorremos los oficios
for row in cursor:
    
    #Agregamos cada oficio
    listaOficios.append(row[0])

#Recorremos la lista para nuestro menu
#Creamos un contador para dar formato al menu
contador = 1
for ofi in listaOficios:
    print(f"{contador}.- {ofi}")
    contador = contador + 1
print("Seleccione una opción")
opcion = int(input())
oficioSeleccionado = listaOficios[opcion - 1]
print(f"Oficio seleccionado: {oficioSeleccionado}")

#Consultamos los empleados con el oficio seleccionado
sql = "select * from EMP where OFICIO=:oficio"
cursor.execute(sql, (oficioSeleccionado,))
print("-----Lista de empleados----")
for row in cursor:
    #print("- " + row[1] + ", Salario: " + str(row[5]))
    print(f"- {row[1]}, Salario: {row[5]}")
    
cursor.close()
connection.close()
print("Fin de programa")