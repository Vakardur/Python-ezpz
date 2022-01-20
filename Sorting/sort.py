"""
Queremos saber el número que tardará cierto algoritmo en ejecutarse.
Hay varias maneras de saber cómo, pero hay una universal: Big O Notation.


"""

from timeit import repeat

list = [4, 5, 5, 4, 4, 45, 5, 6, 7, 7, 3, 3, 3, 5676, 3]


def funcion_x():

    list.sort()

    times = repeat(repeat=3)

    print(times)


funcion_x()
