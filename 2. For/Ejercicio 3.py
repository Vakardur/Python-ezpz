"""Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas."""

# Definimos la entrada de usuario como una variable "impar" como un input de un integer.
impar = int(input("Escriba un número entero positivo:\n"))

# Definimos el for. Para un rango de tamaño 'impar', empezando desde 1, y mostrando hasta el número previsto.
for x in range(1, impar + 1):
    # Verificamos si el número es impar con un "if". Si el remanente del x en el rango no es igual a cero...
    if (x % 2 != 0):
        # ... el programa imprime el número, separándolo con una coma.
        print(x, end=",")
