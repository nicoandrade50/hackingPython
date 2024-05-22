def verificar_robustez_contraseña(contraseña):
    # 1. Verificar si la contraseña tiene al menos 8 caracteres
    longitud_suficiente = len(contraseña) >= 8
    
    # 2. Verificar si la contraseña contiene al menos una letra mayúscula
    contiene_mayusculas = any(c.isupper() for c in contraseña)
    
    # 3. Verificar si la contraseña contiene al menos una letra minúscula
    contiene_minusculas = any(c.islower() for c in contraseña)
    
    # 4. Verificar si la contraseña contiene al menos un dígito
    contiene_digitos = any(c.isdigit() for c in contraseña)
    
    # 5. Verificar si la contraseña contiene al menos un carácter especial
    contiene_caracteres_especiales = any(c in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for c in contraseña)
    
    # Calcular la puntuación sumando los criterios cumplidos
    puntuacion = longitud_suficiente + contiene_mayusculas + contiene_minusculas + contiene_digitos + contiene_caracteres_especiales
    
    # Imprimir si la contraseña es o no es robusta
    if puntuacion >= 5:
        print("¡La contraseña es robusta!")
    else:
        print("La contraseña no es lo suficientemente robusta.")

    # Imprimir la puntuación obtenida
    print("Puntuación de la contraseña:", puntuacion)

# Solicitar al usuario que ingrese la contraseña
contraseña = input("Introduce tu contraseña: ")

# Llamar a la función para verificar la robustez de la contraseña
verificar_robustez_contraseña(contraseña)
