"""HARD QUESTION: el día jueves se adjuntará un archivo con una función para llamar a una API y obtener una lista de usuarios con datos aleatorios. Tenga en consideración que esta lista no tendrá la misma longitud siempre. https://api.namefake.com/
a. Haga una función que tome la lista de los nombres, y los organice por orden alfabético. Replique la función utilizando Lambda.
b. De la lista anterior,
    i.¿Quién son los usuarios con una altura entre 140 y 170?
    ii.¿Quiénes tienen el nombre repetido?
    iii¿Quiénes nacieron entre 1980 y el 2000?
c. Si alguien de la lista tiene un username que incluya las letras k, u, y b, entonces les gusta comer pito. 
Si incluyen las letras a, r, y z, entonces les gusta comerse a Guillo.
    i.De las condiciones brindadas, ¿a quiénes les gusta comer pito, pero no el de Guillo?
"""
import requests
import json

response = requests.get('http://api.name-fake.com/random/random')

json_response = response.json()

print(json_response)