import os 

def solicitarNum():
    n1 = int(input("Ingresa un numero:"))
    n2 = int(input("Ingresa un numero:"))
    return n1, n2

def calculadora(n1, n2, opcion):
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
        return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        return f"{n1}/{n2}={n1/n2}"

def esperar():
    os.system("pause")

def limpiar():
    os.system("cls")