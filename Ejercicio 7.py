#Escriba un programa Python que acepte el radio de un círculo del usuario y calcule el área.
    # Ayuda: from math import pi
print('Bienvenido a la calculadora de áreas ACME.\n')

radius = int(input('Ingrese el radio a calcular.\n'))

from math import pi

Area = pi*radius

print('El área de su círculo es de',Area)