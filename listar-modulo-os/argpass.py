import os
import argparse

def listar_archivos_sensibles(directorio):
    # Definir extensiones de archivos sensibles
    extensiones_sensibles = ['.db', '.pem']

    # Lista para almacenar los archivos sensibles encontrados
    archivos_sensibles = []

    # Recorrer el directorio y subdirectorios
    for ruta_directorio, _, archivos in os.walk(directorio):
        for archivo in archivos:
            if any(archivo.endswith(ext) for ext in extensiones_sensibles):
                archivos_sensibles.append(os.path.join(ruta_directorio, archivo))

    return archivos_sensibles

def main():
    # Crear el objeto ArgumentParser
    parser = argparse.ArgumentParser(description="Buscar archivos sensibles en un directorio.")

    # Agregar un argumento para el directorio
    parser.add_argument("directorio", type=str, help="Directorio a escanear")

    # Analizar los argumentos de la línea de comandos
    args = parser.parse_args()

    # Obtener lista de archivos sensibles
    archivos_encontrados = listar_archivos_sensibles(args.directorio)

    # Mostrar los archivos encontrados
    if archivos_encontrados:
        print("Archivos sensibles encontrados:")
        for archivo in archivos_encontrados:
            print(archivo)
    else:
        print("No se encontraron archivos sensibles.")

if __name__ == "__main__":
    main()
