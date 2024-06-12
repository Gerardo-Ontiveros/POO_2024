"""
3.- 
Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
 palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
 el contenido de la lista en mayusculas
"""
def list():
    try:
        my_list = []

        if my_list == []:
            while True:
                add = input("Ingresa lo que quieres agregar: ")
                my_list.append(add)
                option = input("Deseas agregar algo mas (S/N)? ").upper()
                if option == "N":
                    break
        for i in range(len(my_list)):
            my_list[i] = my_list[i].upper()
        print(my_list)
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
list()