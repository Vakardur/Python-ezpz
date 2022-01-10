"""Escriba un programa que genere un número aleatorio del 1 al 20 y devuelva su factorial"""


import random

x = random.randrange(1,21)
factorial = 1

#for
for i in range(1,x + 1):
    factorial = factorial * i
print("con 'for' el factorial de" ,x, "es", factorial)


#while
counter = x
factorial2 = 1
while counter > 0:
    factorial2 = factorial2*counter
    counter -= 1

print("con 'while', el factorial de", x, 'es', factorial2)

#Ahí tiene su hpta while pintado Ayano .|.
    




