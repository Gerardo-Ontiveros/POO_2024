"""
5.- 
Crear una lista y un diccionario con el contenido de esta tabla: 

  ACCION              TERROR        DEPORTES
  MAXIMA VELOCIDAD    LA MONJA       ESPN
  ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
  RAPIDO Y FURIOSO I  LA MALDICION   ACCION


  imprimir la información
"""

# def peliculas():
  # peliculas = {
  #   "accion":["Maxima Velocidad","Arma Mortal 4", "Rapido y Furioso I"],
  #   "terror":["La monja","El conjuro", "La maldicion"],
  #   "deportes":["ESPN", "Mas Deporte", "Accion"],
  # }

  # print(f"{peliculas['accion' ]}\n")
  # print(f"{peliculas['terror']}\n")
  # print(f"{peliculas['deportes']}")
#peliculas()
import os 
import time

def peliculas():
  while True:
    try:
      peliculas = {
        "accion": ["Maxima Velocidad","Arma Mortal 4", "Rapido y Furioso I"],
        "terror":["La monja","El conjuro", "La maldicion"],
        "deportes":["ESPN", "Mas Deporte", "Accion"],
      }
      print("¿Que categoria deseas ver? \n 1) Accion \n 2) Terror \n 3) Deportes")
      option = input("Tu opcion: ").upper()
      if option == "1" or option == "ACCION":
          print(f"{peliculas['accion']}")
      elif option == "2" or option == "TERROR":
          print(f"{peliculas['terror']}")
      elif option == "3" or option == "DEPORTES":
          print(f"{peliculas['deportes']}")
      else:
         print("Ingresa una opcion valida.... Vuelve a intentarlo.")
      if option in ['1', '2', '3', "ACCION", "TERROR", "DEPORTES"]:
        break
    except Exception as e:
       print(f"Ha ocurrido un error: {e}") 
    finally:
       time.sleep(2)
       os.system("cls")
peliculas()