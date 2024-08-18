import mysql.connector
from mysql.connector import Error
import os

try: 
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "examen"
    )
    cursor = conexion.cursor(buffered=True)
except Error as e:
    print(f"Error {e}")

class Clientes:
    def __init__(self, nif,nombre,direccion,ciudad,tel):
        self.nif = nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.tel = tel

    def insertar(self):
        sql = "INSERT INTO clientes VALUES (%s,%s,%s,%s,%s)"
        val = (self.nif,self.nombre,self.direccion,self.ciudad,self.tel)
        cursor.execute(sql,val)
        conexion.commit()
        return True

    def consultar():
        sql = "SELECT * FROM clientes"
        cursor.execute(sql)
        res = cursor.fetchall()
        return res
    
    def actualizar(self):
        sql = "UPDATE clientes SET nombre = %s, direccion = %s, ciudad =%s, tel=%s  WHERE nif = %s"
        val = (self.nombre, self.direccion,self.ciudad,self.tel,self.nif)
        cursor.execute(sql,val)
        conexion.commit()
        return True

    def eliminar(nif):
        sql = "DELETE FROM clientes WHERE nif = %s "
        val = (nif, )
        cursor.execute(sql,val)
        conexion.commit()
        return True

print("""
    1.- Insertar
    2.- Consultar
    3.- Actualizar
    4.- Eliminar

""")
option = input("Elige una opcion: ")

if option == "1" or option == "INSERTAR":
    os.system("cls")
    nif = input("Ingresa el NIF del usuario (5 digitos): ")
    nombre= input("Ingresa el nombre del cliente: ")
    direccion = input("Ingresa la direccion del cliente: ")
    ciudad = input("Ingresa la ciudad del cliente: ")
    tel = input("Ingresa el telefono del cliente: ")
    req = Clientes(nif,nombre,direccion,ciudad,tel)
    res = req.insertar()
    if res:
        print("Se ha agregado el usuario correctamente")
elif option == "2" or option == "CONSULTAR":
    os.system("cls")
    req = Clientes.consultar()
    for x in req:
        print(f"NIF: {x[0]}")
        print(f"Nombre: {x[1]}")
        print(f"direccion: {x[2]}")
        print(f"Ciudad: {x[3]}")
        print(f"Telefono: {x[4]}")
        print("\n")
    
elif option == "3" or option == "ACTUALIZAR":
    os.system("cls")
    nif = input("Ingresa el NIF del usuario a actualizar: ")
    nombre = input("Ingresa el nuevo nombre: ")
    direccion = input("Ingresa la direccion: ")
    ciudad = input("Ingresa la ciudad: ")
    tel = input("Ingresa el telefono: ")
    req = Clientes(nif,nombre,direccion,ciudad,tel)
    res = req.actualizar()
    if res: 
        print("Se ha actualizado correctamente el usuario... ")

elif option == "4" or option == "Eliminar":
    os.system("cls")
    nif = input("Ingresa el NIF del usuario a eliminar: ")
    req = Clientes.eliminar(nif)
    if req:
        print("El usuario se ha borrado correctamente")