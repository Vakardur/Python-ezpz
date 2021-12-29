# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

print("Programa de las tablas de multiplicar:\n")

número = int(input("Ingrese el número del cual quiere ver las tablas:\n"))

for x in range(1, 11):
    print(número,"x", x, '=', número*x)
