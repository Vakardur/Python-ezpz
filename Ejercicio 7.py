# Escriba un programa Python que acepte el radio de un círculo del usuario y calcule el área.
from math import pi
# Ayuda: from math import pi
print('Bienvenido a la calculadora de áreas ACME.\n')

radius = int(input('Ingrese el radio a calcular.\n'))


Area = pi * radius

print('El área de su círculo es de', Area)
