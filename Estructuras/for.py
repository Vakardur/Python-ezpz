"""
Vamos a partir de la idea de que tenemos que iterar.
¿Qué es iterar?
-> Iterar es cuando nosotros podemos recorrer una secuencia de datos.

Las secuencias de datos pueden ser listas, tuplas, diccionarios, objetos, etc.
"""

lista = ['a', 'b', 'c', 'd', 'e']

# Vamos a usar el for para recorrer la lista
for elemento in lista:
    # elemento solo funciona dentro de for
    # print(elemento)
    pass


# Imprima los numeros de la lista que sean multiplos de dos
lista_2 = [1, 2, 3, 4, 5]

for numero in lista_2:
    if numero % 2 == 0:
        # print(numero)
        pass

# Imprima todos los valores hasta que llegue a Ratón, y luego pare de iterar.
lista_3 = ['Perro', 'Gato', 'Ratón', 'Else', 'Mosca']

for animal in lista_3:
    # print(animal)
    if animal == 'Ratón':
        break


# ¿Cuántos True hay en la lista?
lista_4 = [True, False, True, True, False]

counter = 0
for booleano in lista_4:
    if booleano is True:
        counter += 1

# No se mete un print dentro de un for si no se quiere que se impriman valores en cada iteración
# print(counter)


# Imprima la suma de cada sublista que está en la lista principal => sum()
lista_5 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]

for sublista in lista_5:
    resultado = sum(sublista)
    # print(resultado)
    break


# Imprima el número máximo de cada sublista en la lista principal => max()
lista_6 = [['1', '7'], ['2', '545'], ['3', '15616'], ['0', '4'], ['848', '5']]

lista_nueva = []
for sublista in lista_6:
    lista_nueva.append([int(sublista[0]), int(sublista[1])])

# print(lista_nueva)
for sublista in lista_nueva:
    resultado = max(sublista)
    break
    # print(resultado)

"""
Cada elemento de una lista tiene dos datos asociados a él: su valor, y su posición en la lista.
La posición en las listas, y en general en programación, empiezan desde cero.

Mal => 1, 2, 3, 4, 5
Bien => 0, 1, 2, 3, 4
"""

# Imprima la posición de cada elemento de la lista
# len => longitud de una lista (length)
lista_7 = [1, 2, 3, 4, 5]

for elemento in range(len(lista_7)):
    # print(elemento)
    break

# Imprima las posiciones pares

lista_8 = [6, 7, 8, 9, 10]

for elemento in range(len(lista_8)):
    if elemento % 2 == 0:
        # print(elemento)
        break

"""
HIGH LEVEL

Pythonic code es código que se escribe en una sola línea.
Como Python es tan fácil de leer, entonces la gente se pone a implementar soluciones que ocupen menos espacio de código,
porque le reduce la complejidad.

Muchas estructuras se pueden escribir como una sola linea en Python.

Por ejemplo, 

x = 5
verificacion = None
if x >= 5:
    verificacion = True
else:
    verificacion = False
    
↓ ↓ ↓    
verificacion = True if x >= 5 else False

"""

# inline For simple

lista = [1, 2, 3, 4, 5]

for elemento in lista:
    if elemento % 2 == 0:
        # print(elemento)
        break

# print(True) if (elemento % 2 == 0 for elemento in lista) else print(False)


# inline for con sublistas
lista_5 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]

verificador = None

verificador = True if (sum(sublista) == 2 for sublista in lista_5) else False

# print(verificador)

lista_sumada = [sum(sublista) for sublista in lista_5]


print(lista_sumada)
