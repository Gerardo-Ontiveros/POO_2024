    #Try | Except | Finally 

#Programa para operaciones basicas 
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
    print("Error: Ingresa valores validos")


#try | Except
try: 
    n1 = int(input("ingresa un numero: "))
    n2 = int(input("Ingresa un numero: "))
    res = n1 + n2
    print(res)
except: 
    print("Error: Ingresa valores validos")
finally:
    print("SIEMPRE SE EJECUTA")

#While 
while(True):
    try: 
        n1 = int(input("Ingresa un numero: "))
        n2 = int(input("Ingresa un numero: "))
        res = n1 + n2
        print(res)
        opcion = input("Desea capturar otra operacion (si/no)").lower()
        if opcion == "no":
            break
    except:
        print("Error: Ingresa valores validos")