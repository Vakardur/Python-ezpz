"""Escriba un programa en Python para imprimir todos los números primos entre 0 y 100 e imprima cuántos números primos hay.
"""

cousin_list = []

for Number in range(1, 101):
    count = 0
    for i in range(2, (Number // 2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        cousin_list.append(Number)
        # print(" %d" % Number, end=' ')

cousin_number = 0

for n in cousin_list:
    cousin_number += 1

print(cousin_number)

# No encuentro una forma de imprimir cuántos hay, koroshitekure.
