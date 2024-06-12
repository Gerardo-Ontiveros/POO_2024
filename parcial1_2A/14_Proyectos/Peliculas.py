try:
    from funciones_compartir import agregar_pelicula, actualizar_pelicula, eliminar_pelicula, consultar_pelicula, mostrar_peliculas, limpiar, Vaciar, buscar
    import time 

    limpiar()
    while True:

        try:
            print(".::::::::::::::::::::::::CINEMAX.::::::::::::::::::::::::")
            print("")
            print(":::::::::::::::::::::MENU DE OPCIONES::::::::::::::::::::")
            opcion = input("                         1.-Agregar \n                         2.- Actualizar \n                         3.- Eliminar \n                         4.- Consultar \n                         5.- Mostrar \n                         6.- Buscar \n                        7.- Vaciar \n                         8.- Salir \n                         Opcion:").upper()
            if opcion == "1" or opcion == "AGREGAR":
                agregar_pelicula()         
            elif opcion == "2" or opcion == "ACTUALIZAR":
                actualizar_pelicula()
            elif opcion == "3" or opcion == "ELIMINAR":
                eliminar_pelicula()
            elif opcion == "4" or opcion == "CONSULTAR":
                consultar_pelicula()
            elif opcion == "5" or opcion == "MOSTRAR":
                mostrar_peliculas()
            elif opcion == "6" or opcion == "BUSCAR":
                buscar()
            elif opcion == "7" or opcion == "VACIAR":
                Vaciar()
            elif opcion == "8" or opcion == "SALIR":
                print("Gracias por visitar CINEMAX")
                break
            time.sleep(2)
            limpiar()
            print("Presiona una tecla para continuar...")
            input()
        except Exception as e:
            print("Ha ocurrido un error: ", e)
except Exception as e:
    print("\n Ha ocurrido un error: ", e, "\n")