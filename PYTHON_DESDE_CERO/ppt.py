#Try | Except | Finally

# Programa para operaciones basicas
n1 = int(input("Ingresa un numero: "))
n2 = int(input("Ingresa un numero: "))
res = n1 + n2
print(res)

#Try | Except
try:
    n1 = int(input("Ingresa un numero: "))
    n2 = int(input("Ingresa un numero: "))
    res = n1 + n2 
    print(res)
except:
    print("Ingrese valores validos")

#Try | Except | Finally
try: 
    n1 = int(input("Ingresa un numeroL "))
    n2 = int(input("Ingresa un numeroL "))
    res = n1 + n2 
    print(res)
except:
    print("Ingresa valores validos")
finally: 
    print("ESTO SIEMPRE SE IMPRIME")

#While 
while(True):
    try:
        n1 = int(input("Ingresa un numero: "))
        n2 = int(input("Ingresa un numero: "))
        res = n1 + n2 
        print(res)
        opcion = input("Deseas hacer otra captura(si/no)").lower()
        if opcion == "no":
            break
    except:
        print("Ingresa valores validos")    
