"""Escriba un programa que genere un número aleatorio del 1 al 20 y devuelva su factorial"""

import random

x = random.randrange(1,21)
factorial = 1
for i in range(1,x + 1):
    factorial = factorial * i
print("el factorial de",x,"es", factorial)
