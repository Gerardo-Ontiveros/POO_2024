"""
10.- Crear un programa que solicite 
la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron
"""
j=0
k=0
for i in range(1, 15):
    n = int(input(f"Ingresa la calificacion {i}: "))
    if n < 80:
        j += 1
        print(f"El numero de reprobados fue de {j}")
    elif n > 80:
        k += 1     
        print(f"El numero de aprobados fue de {k}")