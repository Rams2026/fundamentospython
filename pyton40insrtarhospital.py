import oracledb
connection = oracledb.connect(user="system", password="oracle"
                              , dsn="localhost/FREEPDB1")

#Creamos nuestro cursor para las consultas
cursor = connection.cursor() 
print("Codigo de hospital")
HCOD = input() 
print("Nombre: ")
NOM= input() 
print("Direccion")
DIR = input() 
print("Telefono")
TEL = input() 
print("N. CAMA")
NCAMA = input() 

#EN PYTHON TENEMOS UNA FORMA DE CONCATENAR TAMBIEN
#UTILIZANDO SOLAMENTE UN STRING, SIN + Y SIN NADA
#PARA ELLO, SE UTILIZA LA LETRA f FUERA DEL STRING
#Y CADA VARIABLE IRA ENTRE LLAVES DENTRO DEL STRING

sql = f"INSERT INTO hospital VALUES ({HCOD}, '{NOM}', '{DIR}', {TEL}, {NCAMA})"

#Realizamos la acción de insertar

cursor.execute(sql)
connection.commit()

#Realizamos la consulta de seleccion
sql = "select * from HOSPITAL"
cursor.execute(sql)
for row in cursor:
    HCOD = row[0]
    NOM = row[1]
    DIR = row[2]
    TEL = row[3]
    NCAMA = row[4]
    print(f"CODIGO: {HCOD}, Nombre: {NOM}, Direccion: {DIR}, Telefono: {TEL}, Num Cama: {NCAMA}")
cursor.close()
connection.close()
print("Fin dEL PGM")