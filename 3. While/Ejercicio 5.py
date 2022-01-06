"""Siga los siguientes pasos
        a. Ejecute {k: random.randrange(1, 1000) for k in range(100)}. El valor resultante debe ser una lista con cien elementos, del 0 al 100.
        b. De dicha lista, imprima los números pares y que estén en la constante 0.5772156649 (Euler).
        c. De dicha lista, imprima los números impares y que estén en la constante 3.14159 (pi).
"""

import random
lista = {str(k): random.randrange(1, 1000) for k in range(100)}

#for
euler = '0.5772156649'
pi = '3.14159'

lista_pares = []
lista_impares = []

for x in lista.values():
    if str(x) in euler and x % 2 == 0:
        lista_pares.append(x)
    elif str(x) in pi and x % 2 != 0:
        lista_impares.append(x)


print(lista_pares)
print(lista_impares)

#while
lista_2 = {str(k): random.randrange(1, 1000) for k in range(100)}
lista_valores_2 = list(lista_2.values())
lista_pares_2 = []
lista_impares_2 = []

counter = 0
while counter <= 99:
    if str(lista_valores_2[counter]) in euler and lista_valores_2[counter] % 2 == 0:
        lista_pares_2.append(lista_valores_2[counter])
    elif str(lista_valores_2[counter]) in pi and lista_valores_2[counter] % 2 != 0:
        lista_impares_2.append(lista_valores_2[counter])
    counter = counter + 1
    

print(lista_pares_2)
print(lista_impares_2)
print("done!")  



    