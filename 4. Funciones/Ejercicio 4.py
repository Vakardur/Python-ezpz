"""Haga una función que retorne el número de veces que un número aleatorio del 1 al 10 aparezca en 
otro número aleatorio de 10000. Replique la función utilizando Lambda."""


import random

#Función normal

rand_number = random.randint(1,10)
rand_big = random.randint(1,10000)

def frequency (x):
    counter = 0
    for x in range(1,rand_big):
        if str(rand_number) in str(rand_big):
            counter += 1
    return counter

print(rand_number)
print(rand_big)

print(frequency(rand_number))


"""Ok, no sé si la lógica que estoy implementando tiene sentido o no. Siempre me imprime 0. """

#Función lambda

"""pending"""