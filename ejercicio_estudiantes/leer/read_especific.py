def leer_linea_especifica(archivo, numero_linea):
    with open(archivo, "r") as archivo:
        for indice, linea in enumerate(archivo):
            if indice == numero_linea:
                print(linea.rstrip())
                break
        else:
            print("Número de línea fuera de rango.")

archivo = "estudiantes.txt" 
numero_linea = int(input("Ingrese el número de línea que desea leer: "))

leer_linea_especifica(archivo, numero_linea)


