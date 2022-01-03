"""Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces. """


# Primero definimos la variable "Word" como un input en forma de string.
Word = str(input('Escriba una palabra:\n'))

# Después, empleamos el for. Entonces, for itera "palabra" en un rango de 10 veces.
for palabra in range(10):
    # Para cada iteración, el for imprime la variable "Word."
    print(Word)
