"""
1.- 

 Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

 a.- Recorrer la lista y mostrarla
 b.- hacer una funcion que recorra la lista de numeros y devuelva un string
 c.- ordenarla y mostrarla
 d.- mostrar su longitud
 e.- buscar algun elemento que el usuario pida por teclado
"""

#A)
numeros=[4,1,3,5,0,8,7,6]


def recorrer_lista():
    try:
        for i in numeros:
            print(i)
    #     if i > 0:
    #        num.append(i)
    # print(num)
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")


#B)
def recorrer_lista():
    try:
        num = []
        for i in numeros:
            if i > 0:
                num.append(i)
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")


#C)
def ordernar_lista():
    try:
        numeros.sort()
        print(numeros)
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")


#D)
#Forma 1

def mostrar_longitud():
    try:
        count = 0
        for value in numeros:
            count += 1
        print(count)
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
mostrar_longitud()

#Forma 2
from operator import length_hint
def mostrar_long2():
    try:
        length_hint(numeros)
    except Exception as e:
        print(f"Ha ocurrido un error {e}")


#E)
def encontrarnumero():
    try:
        n = int(input("¿Que numero deseas buscar?:"))

        while True:
            if n in numeros: 
                print(f"El numero {n} se econtro en la posision {numeros.count(n)} vez/ces")
                for i in range(len(numeros)):
                    if numeros[i] == n:
                        print(f"Se encontro en la posicion {i}")
                break
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")


print("Que accion deseas realizar? \n 1) Recorrer lista \n 2) Recorrer lista (String) \n 3) Ordenar lista \n 4) Mostrar tamaño \n 5) Encontrar numero \n")
option = input("Tu opcion: ")

if option == '1':
    recorrer_lista()
elif option == '2':
    recorrer_lista()
elif option == '3':
    ordernar_lista()
elif option == '4':
    mostrar_long2()
elif option == '5':
    encontrarnumero()
