# Funciones

# Una función es una agrupación de instrucciones ejecutable, repetible, reciclable, y atómica.
# Atómica es que únicamente es esa y esa función. No puede llamar una función igual dentro del mismo archivo .py

# Nomenclatura

# def nombre_funcion(parametros):
#    instrucciones
#    return valor

x = 2
y = 3


def suma(x, y):
    return x + y


suma(x, y)

# Los parametros de una función son los valores que se le pasan a la función cuando se llama.
# Los parámetros de la función sólo se pueden llamar dentro de la función.
# Los parámetros de la función, en Python, pueden no ser utilizadas.

x = 2
y = 3
z = 5


def resta(x, y):
    return x - y


# Con asignación de variables
area = 0


def get_area(alto, largo):
    return alto * largo


area = 0


# func para calcular el area de un triangulo
def area_triangulo(base, altura):
    return base * altura / 2


area_triangulo(3, 3)

# Funciones con parametros por defecto


def area_circulo(altura, radio, pi=3.14):
    return pi * radio ** 2


area_circulo(radio=3, altura=5)

# LAMBDA

suma_lambda = (lambda x, y: x + y)

suma_lambda(2, 2)


lista = [4, 5, 6]
max(lista, key=lambda x: x - 5 if x % 2 == 0 else x)

dictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}

dictionary['a']

# reverse es para cambiar de menor a mayor, a mayor a menor
y = sorted(dictionary, key=lambda x: dictionary[x] % 3, reverse=True)
print(y)


filtrado = filter(lambda x: dictionary[x] % 2 == 0, dictionary)
print(list(filtrado))
