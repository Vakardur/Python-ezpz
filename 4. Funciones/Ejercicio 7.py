""" Haga una función que obtenga el máximo valor de la siguiente lista con base a su segundo valor por cada elemento. 
Replique cada función utilizando Lambda. Repita el ejercicio con el valor mínimo."""

lista = [ [ 1, 2, '3' ] , [3, 4, '5'], [5, 6, '7'], [7, 8, '9'], [9, 10, 'F'] ]
#You sneaky little shit. Usando dizque ‘’ en vez de ''. Someday, you will pay.

#Normal
def MaxVal(sublist): 
    return max(lista)
    
print(MaxVal(lista))

#Lambda

print('lambda:',max(lista, key=lambda x: x[1]))