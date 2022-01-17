"""HARD QUESTION: el día jueves se adjuntará un archivo con una función para llamar a una API y obtener una lista de usuarios con datos aleatorios. 
Tenga en consideración que esta lista no tendrá la misma longitud siempre. https://api.namefake.com/
a. Haga una función que tome la lista de los nombres, y los organice por orden alfabético. Replique la función utilizando Lambda.
b. De la lista anterior,
    i.¿Quién son los usuarios con una altura entre 140 y 170?
    ii.¿Quiénes tienen el nombre repetido?
    iii¿Quiénes nacieron entre 1980 y el 2000?
c. Si alguien de la lista tiene un username que incluya las letras k, u, y b, entonces les gusta comer pito. 
Si incluyen las letras a, r, y z, entonces les gusta comerse a Guillo.
    i.De las condiciones brindadas, ¿a quiénes les gusta comer pito, pero no el de Guillo?
"""
import json
import requests
import random

list_size = random.randint(1,4)
lista = []
print('This list contains',list_size,'names.')
for name in range(0,list_size):
    response = requests.get('http://api.namefake.com/random/random')
    json_response = response.json()
    lista.append(json_response)

def Height(x):
    l = len(lista)
    for height in range(0,l):
        if 170> lista[] > 140:
           return height 

print(Height(lista))

#ok, i'm out. Conseguí llamar a la API, pero paila. 