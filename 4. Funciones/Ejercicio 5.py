"""Haga una función que organice la siguiente lista con base a su segundo valor por cada elemento de menor a mayor. 
Replique cada función utilizando Lambda.
"""
lista = [('Inglés', 88), ('Ciencias', 90), ('Matemáticas', 97), ('Ciencias sociales', 82)]

#Normal
def Sort(sublist):
    l = len(sublist)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sublist[j][1] > sublist[j + 1][1]):
                tempo = sublist[j]
                sublist[j]= sublist[j + 1]
                sublist[j + 1]= tempo
    return sublist

print(Sort(lista))

#Fucking lists, fucking hate lists, all my homies hate lists.

#Lambda


