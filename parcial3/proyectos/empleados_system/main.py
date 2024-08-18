import mysql.connector
import os
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host='localhost',
        database='mi_empresa',
        user='root',
        password=''
    )
    if conexion.is_connected():
        print("Conexión exitosa a la base de datos")
except Error as e:
    print(f"Error al conectar a la base de datos: {e}")

def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")

class Empleados:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def crear_empleado(self):
        cursor = conexion.cursor()
        query = "INSERT INTO empleados (nombre, puesto, salario) VALUES (%s, %s, %s)"
        valores = (self.nombre, self.puesto, self.salario)
        cursor.execute(query, valores)
        conexion.commit()
        return True

    @staticmethod
    def leer_empleados():
        cursor = conexion.cursor()
        query = "SELECT * FROM empleados"
        cursor.execute(query)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Puesto: {fila[2]}, Salario: {fila[3]}")
        return True


    def actualizar_empleado(self, id):
        cursor = conexion.cursor()
        query = "UPDATE empleados SET nombre = %s, puesto = %s, salario = %s WHERE id = %s"
        valores = (self.nombre, self.puesto, self.salario, id)
        cursor.execute(query, valores)
        conexion.commit()
        return True

    @staticmethod
    def eliminar_empleado(id):
        cursor = conexion.cursor()
        query = "DELETE FROM empleados WHERE id = %s"
        valor = (id,)
        cursor.execute(query, valor)
        conexion.commit()
        return True

def menu():
    if conexion:
        while True:
            os.system("cls")
            print("\n--- Menú de Opciones ---")
            print("1. Crear empleado")
            print("2. Leer empleados")
            print("3. Actualizar empleado")
            print("4. Eliminar empleado")
            print("5. Salir")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                os.system("cls")
                nombre = input("Nombre: ")
                puesto = input("Puesto: ")
                salario = input("Salario: ")
                req = Empleados(nombre,puesto,salario)
                res = req.crear_empleado()
                if res:
                    print("Trabajador agregado exitosamente ✅")
                    input("Presiona una tecla...")
            elif opcion == '2':
                os.system("cls")
                req = Empleados.leer_empleados()
                if req:
                    print(req)
                    input("Presiona una tecla...")
            elif opcion == '3':
                os.system("cls")
                id = input("ID del empleado a actualizar: ")
                nombre = input("Nuevo nombre: ")
                puesto = input("Nuevo puesto: ")
                salario = input("Nuevo salario: ")
                req = Empleados(nombre,puesto,salario)
                res = req.actualizar_empleado(id)
                if res:
                    print("El empleado se ha actualizado correctamente ✅")
                    input("Presiona una tecla...")
            elif opcion == '4':
                os.system("cls")
                id = input("ID del empleado a eliminar: ")
                req = Empleados.eliminar_empleado(id)
                if req:
                    print("Empleado eliminado correctamente")
                    input("Presiona una tecla...")
            elif opcion == '5':
                cerrar_conexion(conexion)
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()