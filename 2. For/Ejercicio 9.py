"""Escriba un programa en Python para imprimir todos los números primos entre 0 y 100 e imprima cuántos números primos hay.
"""

for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = ' ')

#No encuentro una forma de imprimir cuántos hay, koroshitekure.