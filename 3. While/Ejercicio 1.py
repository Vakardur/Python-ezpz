"""Escriba un programa para imprimir un número natural como input en orden descendente, hasta llegar a 0."""

número = int(input("Escriba el número: \n"))

#for

for x in range(número, -1, -1):
    print(x)

#while

número_2 = int(input("Escriba el segundo número: \n"))

while número_2 > -1:
    print(número_2)
    número_2 = número_2 - 1
   
