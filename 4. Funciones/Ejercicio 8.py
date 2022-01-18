"""Con la siguiente lista y con base a su segundo valor por cada elemento del diccionario, 
y replicando cada punto utilizando Lambda,"""

lista = [
    {'bisiante': 'Nokia',
     'model': 216, 
     'color': 'Black'
     }, 

    {'bisiante': 'Mi Max', 
     'model': 2, 
     'color': 'Gold'
     }, 

    {'bisiante': 'Samsung',
     'model': 7, 
     'color': 'Blue'
     }
     ]

"""
1. Obtenga el registro del diccionario con el modelo más grande.
2. Obtenga todos los registros que tengan modelos pares.
"""


#1. 

def SortDict(list):
    return max((x['model']) for x in lista)

print(SortDict(lista))

lamdict = print(max(lista, key= lambda dict: dict['model']))

print(lamdict)

#2

"""def EvenMod(list):
    l = len(lista)
    for value in range(0,l):
        if value in lista[1] % 2 == 0:
            print(value)

print(EvenMod(lista))"""