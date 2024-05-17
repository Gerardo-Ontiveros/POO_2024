'''
    Ciclo while es estructura interativa que se ejecuta X veces siempre y cuando la condicion se cumpla
    y se seguira ejecutando tantas veces como sea TRUE la condicion  

    Sintaxis:
        while condicion:
            {...bloque de codigo...}
'''

#Ejemplo 1 Crear que imprima en pantalla 5 veces el @
caracter = 1

while caracter <= 5:
    print('@')
    caracter += 1

#Ejemplo 2 Crear un programa que imprima los numeros del 1 al 5 y los sume al final debe imprimir la suma

suma = 0
i = 1
while i <= 5:
    print(i)
    suma += i
    i += 1
    
print(f"La suma es: {suma}")

#Ejemplo 3 Crear un programa que imprima la tabla de multiplicar que el usuario desee

multi = 1 
tabla = int(input("Ingrese la tabla de multiplicar: "))
while multi <= 10: 
    print(f"{tabla} x {multi} = {tabla * multi}")
    multi += 1

