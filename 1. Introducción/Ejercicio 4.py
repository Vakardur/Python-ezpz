# Escriba un programa Python para probar si un número está dentro de 100 de 1000 o 2000.

import math
print("Programa de detección de numeritos y tal.\n")
try:
    value = int(input('escriba un número\n'))
except Exception:
    raise NameError('Entrada no valida')
val_1000 = math.isclose(value, 1000, abs_tol=499)
val_2000 = math.isclose(value, 2000, abs_tol=499)

if val_1000 is True:
    print('El número está más cerca a mil.')
if val_2000 is True:
    print('El número está más cerca a dosmil.')
else:
    print('El número está fuera del rango.')
