
with open("estudiantes.txt", "r") as archivo:
    lineas = archivo.readlines()[:5]  
    for linea in lineas:
        print(linea)
