"""Escriba un programa que agregue el tipo de elementos de una lista a una nueva lista
        A. Por ejemplo, si tengo la lista [True, ‘2’, 2], debería tener una nueva lista que tuviese [<class ‘bool’>, <class ‘str’>, <class ‘int’>]
        B. La lista la debe hacer con tres For, cada uno de 1 a 10.
            i. El primer For debe generarle valores aleatorios enteros. 
            ii. El segundo For debe generarle valores aleatorios booleanos.
            iii. El tercer For debe generarle valores aleatorios decimales (float).
"""

import random

lista_all = []
"""FOR"""
#Valores enteros
for x in range(1,11):
    x = random.randrange(1,11)
    lista_all.append(x)
#Valores booleanos
for x in range(1,11):
    x = random.choice([True, False])
    lista_all.append(x)
#Valores decimales (float)
for x in range(1,11):
    x = round(random.random(),2)
    lista_all.append(x)

print("Esta lista fue realizada con for:")
print(lista_all, sep=" ")


"""WHILE"""
lista_all_2 = []

count_1 = 0
count_2 = 0
count_3 = 0

# Valores enteros
while count_1 < 11:
    value_1 = random.randrange(1,11)
    lista_all_2.append(value_1)
    count_1 = count_1 + 1
# Valores booleanos  
while count_2 < 11:
    value_2 = random.choice([True, False])
    lista_all_2.append(value_2)
    count_2 = count_2 + 1
# Valores float
while count_3 < 11:
    value_3 = round(random.random(),2)
    lista_all_2.append(value_3)
    count_3 = count_3 + 1
print("Esta lista fue realizada con while:")
print(lista_all_2, sep=" ")