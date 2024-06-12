import os 
import time
import math


def solicitarNum():
    n1 = int(input("Ingresa un numero:"))
    n2 = int(input("Ingresa un numero:"))
    return n1, n2

def num():
    n1 = int(input("Ingresa un numero: "))
    return n1

def calculadora(opcion):
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        n1,n2 = solicitarNum()
        return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        n1,n2 = solicitarNum()
        return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
        n1,n2 = solicitarNum()
        return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        n1,n2 = solicitarNum()
        return f"{n1}/{n2}={n1/n2}"
    elif opcion=="5" or opcion=="**" or opcion=="EXPONENTE":
        n1,n2 = solicitarNum()
        return f"{n1}^{n2}={n1**n2}"
    elif opcion=="6" or opcion=="RAIZ":
        n1 = num()
        return f"√{n1}={math.sqrt(n1)}"

def esperar():
    os.system("pause")

def limpiar():
    os.system("cls")

peliculas = []
def agregar_pelicula():
    nombre = input("Ingresa el nombre de la pelicula: ")
    genero = input("Ingresa el genero de la pelicula: ")
    anio = int(input("Ingresa el año de la pelicula: "))
    peliculas.append([nombre, genero, anio])
    print(f"La pelicula {nombre} se agrego correctamente")

def actualizar_pelicula():
    nombre = input("Ingresa el nombre de la pelicula a actualizar: ")
    for pelicula in peliculas:
        if nombre == pelicula[0]:
            print(f"Nombre: {pelicula[0]}")
            print(f"Genero: {pelicula[1]}")
            print(f"Año: {pelicula[2]}")
            print("Ingresa los nuevos datos de la pelicula")
            nombre = input("Ingresa el nombre de la pelicula: ")
            genero = input("Ingresa el genero de la pelicula: ")
            anio = int(input("Ingresa el año de la pelicula: "))
            peliculas[peliculas.index(pelicula)] = [nombre, genero, anio]
            print(f"La pelicula {nombre} se actualizo correctamente")
            return
    print(f"La pelicula {nombre} no se encontro")

def eliminar_pelicula():
    nombre = input("Ingresa el nombre de la pelicula a eliminar: ")
    for pelicula in peliculas:
        if nombre == pelicula[0]:
            peliculas.remove(pelicula)
            print(f"La pelicula {nombre} se elimino correctamente")
            return
    print(f"La pelicula {nombre} no se encontro")

def consultar_pelicula(): 
    nombre = input("Ingresa el nombre de la pelicula a consultar: ")
    for pelicula in peliculas:
        if nombre == pelicula[0]:
            print(f"Nombre: {pelicula[0]}")
            print(f"Genero: {pelicula[1]}")
            print(f"Año: {pelicula[2]}")
            return
    print(f"La pelicula {nombre} no se encontro")

def mostrar_peliculas():
    for i in peliculas:
        if peliculas == []:
            print("No hay peliculas en la lista")
        print(f"Nombre: {i[0]}")
        print(f"Genero: {i[1]}")
        print(f"Año: {i[2]}")
        print("")

def Vaciar():
    print("PRESIONA UNA TECLA PARA CONTINUAR...")
    os.system('pause')
    peliculas.clear()
    print("La cartelera fue eliminada")

def buscar():
    nombre = input("Ingresa el nombre de la pelicula: ")
    if nombre in peliculas:
        pos = peliculas.index(nombre)
        print(f"La pelicula es: {peliculas[pos]}")
    else:
        print("No se encontro la pelicula")