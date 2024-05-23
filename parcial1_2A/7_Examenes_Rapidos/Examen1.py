


new_paciente = "SI"
paciente = 0
sSis = 0
sDia = 0
m = 1
while new_paciente == "SI":
    paciente += 1
    name = input("Ingresa el nombre: ")
    ts = input("Ingresa el tipo de sangre: ")
    for i in range(3):
        print(f"MEDICION {m}")
        sis = int(input("Ingresa el valor de SIStolica: "))
        sSis += sis
        dia = int(input("Ingresa el valor de DIAtolica: "))
        sDia += dia
        m +=1

    
    promedioSis = sSis / 3
    promedioDia = sDia / 3

    print(f"Nombre: {name}")
    print(f"Tipo de sangre: {ts}")
    if promedioSis <= 120 and promedioDia <= 80:
        print("Presenta una precion normal")

    print(f"El promedio de la SIStolica es de: {promedioSis}")
    print(f"El promedio de la DIAtolica es de: {promedioDia}")

    new_paciente = input("Desea agregar otra captura? (SI/NO): ").upper()


print(f"El numero de pacientes fue de: {paciente}")