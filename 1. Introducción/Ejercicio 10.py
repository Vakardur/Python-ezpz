# HARD QUESTION: escriba un programa en Python para calcular la hipotenusa de un triángulo rectángulo
import math
from math import sqrt

print('Calculadora re-piragórica. Easy, peasy.')

cateto1 = int(input('inserte el valor del primer cateto:\n'))
cateto2 = int(input('inserte el valor del segundo cateto:\n'))

hipotenusa = round(math.sqrt(cateto1**2+cateto2**2),2)

print('La hipotenusa de este triángulo mide',hipotenusa, 'unidades.')
