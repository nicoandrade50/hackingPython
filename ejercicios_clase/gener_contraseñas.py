import random


caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"


longitud = int(input("Introduce la longitud de la contraseña: "))


contraseña = ""
for i in range(longitud):
    contraseña += random.choice(caracteres)


print("Tu nueva contraseña es:", contraseña)
