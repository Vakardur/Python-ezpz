"""Imprima el siguiente patrón con For"""

asterisk = int(input("Escriba cuántas filas quiere\n"))

for x in range(asterisk):
    for y in range(0, x + 1):
        print("*", end='')
    print("\r")
for x in range(asterisk, 0, -1):
    for y in range(0, x - 1):
        print("*", end='')
    print("\r")
