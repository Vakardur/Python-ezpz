"""HARD QUESTION: el día jueves se adjuntará un archivo con una función para llamar a una API y obtener una lista de usuarios con datos aleatorios.
Tenga en consideración que esta lista no tendrá la misma longitud siempre. https://api.namefake.com/
a. Haga una función que tome la lista de los nombres, y los organice por orden alfabético.
b. De la lista anterior,
    i.¿Quién son los usuarios con una altura entre 140 y 170?
    ii.¿Quiénes tienen el nombre repetido?
    iii¿Quiénes nacieron entre 1980 y el 2000?
c. Si alguien de la lista tiene un username que incluya las letras k, u, y b, entonces les gusta comer pito.
Si incluyen las letras a, r, y z, entonces les gusta comerse a Guillo.
    i.De las condiciones brindadas, ¿a quiénes les gusta comer pito, pero no el de Guillo?
"""
import requests
from datetime import datetime
import random


people_list = []


for x in range(0, random.randint(2, 5)):
    request = requests.get(
        'http://api.namefake.com/english-united-states/random')
    if request.status_code == 200:
        response = request.json()
        new_list = [response['name'], response['height'],
                    datetime.strptime(response['birth_data'], '%Y-%m-%d')]
        people_list.append(new_list)

print(people_list)


def sort_alphabet_lambda():
    return sorted(people_list, key=lambda x: x[0])


def get_height_lambda():
    return list(filter(lambda x: 140 <= x[1] <= 170, people_list))


def get_compared_dates():
    return list(filter(lambda x: datetime(1980, 1, 1) <= x[2] <= datetime(2000, 1, 1), people_list))


def check_pito_eater():
    pito_eaters = []
    for item in people_list:
        if item[0].find('k') != -1 or item[0].find('u') != -1 or item[0].find('b') != -1:
            pito_eaters.append(item[0])


print(sort_alphabet_lambda())
print(get_height_lambda())
print(get_compared_dates())
print(check_pito_eater())
