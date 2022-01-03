"""Dado un número, cuente el número total de dígitos del mismo. Ejemplo, el número es 81195, por lo que la salida debería ser 5."""

# ¿Estamos seguros de que aquí se necesita un for?

numero = int(input("Escriba un número:\n"))
print(len(str(numero)))

# Se puede hacer de varias maneras, pero la idea es que practique el for
# La idea era hacer esto ↓
numero = str(numero)
counter = 0
for char in range(len(numero)):
    counter += 1

print(counter)
