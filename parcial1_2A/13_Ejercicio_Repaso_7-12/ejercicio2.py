"""
2.- 
Escribir un programa  que añada valores a una lista mientras que su longitud 
 sea menor a 120, y luego mostrar la lista: Usar un while y for
"""
def add_valores():
    try:
        num=[]
        value = 0
        while len(num) < 120:
            num.append(value)
            value += 1
        print("While:")
        print(num)
        for item in range(120):
            num.append(item)
        print("\n For:")
        print(num)

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
add_valores()
