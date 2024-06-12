"""
4.- 
 Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
  y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

"""
my_list = ["hola", "mundo"]
cadena = "que tal"
entero = 10
logico = False

def tipo_dato(variable):
    if isinstance(variable, bool):
        print(f"La variable es un bool")
    elif isinstance(variable, str):
        print("La variable es una cadena")
    elif isinstance(variable, list):
        print("La variable es una lista")
    elif isinstance(variable, int):
        print("La variable es un entero")

tipo_dato(my_list)
tipo_dato(cadena)
tipo_dato(entero)
tipo_dato(logico)