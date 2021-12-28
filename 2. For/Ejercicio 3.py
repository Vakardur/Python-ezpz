#Escribir un programa que pida al usuario un número entero positivo y 
#muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

Entrada_Numerica = int(input('Escriba un número entero positivo: \n'))

for n in range(1, Entrada_Numerica):
    if n % 2 is not 0:
        print(n,",")
