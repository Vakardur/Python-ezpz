"""Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10."""

print("Programa de las tablas de multiplicar:\n")

for x in range(1, 10 + 1):
    for y in range(1, 10 + 1):
        print(x, 'x', y, '=', x * y,)
    print('')
