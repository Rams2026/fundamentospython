import oracledb

class OracleEmpleado:
    #Declarar las propiedades en el Constructor
    def __init__(self):
        self.connection = oracledb.connect(user="system", password="oracle"
                              , dsn="localhost/FREEPDB1")
    
    #Los metodos que deseemos.
    def eliminarEmpleado(self, idEmpl):
        #Creamos un nuevo cursor: Entrar
        cursor = self.connection.cursor()
        sql = "delete from EMP where EMP_NO=:empno"
        cursor.execute(sql, (idEmpl,))
        registros = cursor.rowcount #rowcountpara saber cuantos registros fueron afectados
        self.connection.commit()
        #Cerramos el cursor: Salimos y liberamos recursos DDBB
        cursor.close()
        return registros