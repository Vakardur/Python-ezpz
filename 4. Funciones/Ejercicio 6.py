"""Haga una función que organice la siguiente lista con base a su segundo valor por cada elemento de mayor a menor. 
Replique cada función utilizando Lambda.
"""
lista = [['Cardenas', 478], ['Alejo', 536], ['Joshua', 529]]


#normal
def MaxSort(sublist):
    l = len(sublist)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sublist[j][1] < sublist[j + 1][1]):
                tempo = sublist[j]
                sublist[j]= sublist[j + 1]
                sublist[j + 1]= tempo
    return sublist

print(MaxSort(lista))

#lambda
print('lambda imprime')

print(sorted(lista, key=lambda x: x[1],reverse=True))

