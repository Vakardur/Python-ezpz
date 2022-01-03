"""Escribir un programa que pida al usuario un número entero y 
muestre por pantalla un triángulo rectángulo dibujado con asteriscos, de altura el número introducido."""

# Definimos la variable de entrada "asterisk" como un input de un integer.
asterisk = int(input("Escriba cuántas filas quiere\n"))

# Este ejercicio pide un nested for. Uno para las columnas, y el otro para las filas. El loop interno será ejecutado una vez para cada iteración del
# loop externo. Así, la altura del triángulo es definida por el primer for, definiendolo como un rango de tamaño "asterisk"...
for x in range(asterisk):
    # ...para posteriormente, en cada iteración del programa, agregar + 1 a la iteración X del for previo.
    for y in range(x + 1):
        # para finalmente imprimir un asterisco "*", separado por un espacio "end(" ")"
        print("*", end=' ')
    # y emplear este print para imprimir los asteriscos en las columnas.
    print("")
