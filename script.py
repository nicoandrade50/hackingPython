import argparse

def verificar_robustez_clave(clave):
    longitud = len(clave)
    tiene_mayusculas = any(c.isupper() for c in clave)
    tiene_minusculas = any(c.islower() for c in clave)
    tiene_digitos = any(c.isdigit() for c in clave)
    tiene_simbolos = any(c in '!@#$%^&*()-_=+[{]}\\|;:\'",<.>/?' for c in clave)


    if longitud < 8:
        return "La clave es demasiado corta. Debe tener al menos 8 caracteres."

    elif not tiene_mayusculas or not tiene_minusculas:
        return "La clave debe contener tanto letras mayúsculas como minúsculas."

    elif not tiene_digitos:
        return "La clave debe contener al menos un dígito."

    elif not tiene_simbolos:
        return "La clave debe contener al menos un símbolo especial."
    else:
        return "La clave es lo suficientemente robusta."

def main():

    parser = argparse.ArgumentParser(description="Verificar la robustez de una clave.")


    parser.add_argument("clave", type=str, help="Clave a verificar")


    args = parser.parse_args()


    resultado = verificar_robustez_clave(args.clave)


    print(resultado)

if __name__ == "__main__":
    main()
