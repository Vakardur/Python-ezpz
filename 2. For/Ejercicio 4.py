#Escribir un programa que pida al usuario un número entero y 
#muestre por pantalla un triángulo rectángulo dibujado con asteriscos, de altura el número introducido.

Número = int(input("Escriba cuántas filas quiere\n"))

for x in range(1, Número + 1):
    for y in range (1, x + 1):
        print(y,end='')
    print("")
