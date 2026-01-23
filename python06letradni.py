
import datetime
def obtener_dia_nacimiento():
    #pedir fecha de nacimiento 
    fecha_str = input("teclea fecha de nacimiento (dd/mm/aaaa): ")
    print (fecha_str)
    fecha_nac = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")