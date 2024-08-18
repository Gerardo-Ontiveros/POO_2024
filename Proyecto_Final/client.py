import mysql.connector

class Usuarios:
    def __init__(self, rfc, nombre,apellido, correo, telefono, direccion, ciudad, estado,cp,pais, id=None):
        self.id = id
        self.rfc = rfc
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.ciudad = ciudad
        self.estado = estado
        self.cp = cp
        self.pais = pais

    def obtener_conexion():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="", 
            database="frutimax"
        )

    @staticmethod
    def verificar_credenciales(correo, contrasena):
        conexion = Usuarios.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        query = "SELECT * FROM clients WHERE email = %s AND password = %s"
        cursor.execute(query, (correo, contrasena))
        usuario = cursor.fetchone()
        cursor.close()
        conexion.close()
        return usuario
    
    @staticmethod
    def verificar_credenciales_employee(correo, contrasena):
        conexion = Usuarios.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        query = "SELECT * FROM employee WHERE idEmployee = %s AND password = %s"
        cursor.execute(query, (correo, contrasena))
        usuario = cursor.fetchone()
        cursor.close()
        conexion.close()
        return usuario


class Clients(Usuarios):
    def __init__(self,rfc, nombre,apellido, correo, contrasena, telefono, direccion, ciudad, estado,cp,pais, id=None):
        super().__init__(nombre, rfc, nombre,apellido, correo, telefono, direccion, ciudad, estado,cp,pais, id=None)

        self.contrasena = contrasena
    def crear(self):
        conexion = Usuarios.obtener_conexion()
        cursor = conexion.cursor()
        query = """
            INSERT INTO clients VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = (self.nombre, self.apellido, self.telefono, self.correo, self.contrasena, self.direccion,self.ciudad,self.estado,self.cp,self.pais)
        cursor.execute(query, values)
        conexion.commit()
        self.id = cursor.lastrowid
        cursor.close()
        conexion.close()
        return self.id is not None

    def actualizar(self, id_usuario):
        conexion = Usuarios.obtener_conexion()
        cursor = conexion.cursor()
        query = """
            UPDATE clients
            SET nombre = %s, correo = %s, contrasena = %s, rol = %s
            WHERE id = %s
        """
        values = (self.nombre, self.correo, self.contrasena, id_usuario)
        cursor.execute(query, values)
        conexion.commit()
        cursor.close()
        conexion.close()
        return cursor.rowcount > 0

    @staticmethod
    def eliminar(id_usuario):
        conexion = Usuarios.obtener_conexion()
        cursor = conexion.cursor()
        query = "DELETE FROM clients WHERE id = %s"
        cursor.execute(query, (id_usuario,))
        conexion.commit()
        cursor.close()
        conexion.close()
        return cursor.rowcount > 0

class employee(Usuarios):
    def __init__(self,rfc, nombre,apellido, correo, contrasena, telefono, direccion, ciudad, estado,cp,pais, id=None):
        super().__init__(nombre, rfc, nombre,apellido, correo, telefono, direccion, ciudad, estado,cp,pais, id=None)

        self.contrasena = contrasena
    def crear(self):
        conexion = Usuarios.obtener_conexion()
        cursor = conexion.cursor()
        query = """
            INSERT INTO employee VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = (self.nombre, self.apellido, self.telefono, self.correo, self.contrasena, self.direccion,self.ciudad,self.estado,self.cp,self.pais)
        cursor.execute(query, values)
        conexion.commit()
        self.id = cursor.lastrowid
        cursor.close()
        conexion.close()
        return self.id is not None

    def actualizar(self, id_usuario):
        conexion = Usuarios.obtener_conexion()
        cursor = conexion.cursor()
        query = """
            UPDATE employee
            SET nombre = %s, correo = %s, contrasena = %s,
            WHERE id = %s
        """
        values = (self.nombre, self.correo, self.contrasena, id_usuario)
        cursor.execute(query, values)
        conexion.commit()
        cursor.close()
        conexion.close()
        return cursor.rowcount > 0

    @staticmethod
    def eliminar(id_usuario):
        conexion = Usuarios.obtener_conexion()
        cursor = conexion.cursor()
        query = "DELETE FROM employee WHERE id = %s"
        cursor.execute(query, (id_usuario,))
        conexion.commit()
        cursor.close()
        conexion.close()
        return cursor.rowcount > 0

