def listar_archivos_sensibles(directorio):
    extensiones_sensibles = ['.db', '.sql', '.key', '.pem']
    archivos_sensibles = []
    for ruta_directorio, _, archivos in os.walk('C:\\Users\\Nico\\AppData\\Local\\Programs\\Python\\Python312'):
        for archivo in archivos:
            if any(archivo.endswith(ext) for ext in extensiones_sensibles):
                archivos_sensibles.append(os.path.join(ruta_directorio, archivo))
    return archivos_sensibles



directorio_a_escanear = 'C:\\Users\\Nico\\AppData\\Local\\Programs\\Python\\Python312'
archivos_encontrados = listar_archivos_sensibles(directorio_a_escanear)

if archivos_encontrados:
    print("Archivos sensibles encontrados:")
    for archivo in archivos_encontrados:
        print(archivo)
else:
    print("No se encontraron archivos sensibles.")
