#Escribir un programa que pida al usuario un número entero positivo y 
#muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

asterisk = int(input("Escriba cuántas filas quiere\n"))

for x in range(asterisk):
    for y in range (x+1):
        print("*",end='')
    print("")