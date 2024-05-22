def leer_y_escribir_linea_especifica(archivo_origen, archivo_destino, numero_linea):
    with open(archivo_origen, "r") as archivo:
        for indice, linea in enumerate(archivo):
            if indice == numero_linea:
                with open(archivo_destino, "w") as archivo_dest:
                    archivo_dest.write(linea)
                print("Línea escrita en el archivo destino.")
                break
        else:
            print("Número de línea fuera de rango.")

archivo_destino = "linea_seleccionada.txt"  # Nombre del archivo de destino
numero_linea = int(input("Ingrese el número de línea que desea leer: "))

leer_y_escribir_linea_especifica(archivo_origen, archivo_destino, numero_linea)
