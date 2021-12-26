# Escriba un programa en Python para calcular la suma de tres números dados, si los valores son iguales, devuelva tres veces su suma.
print('Sumadora express.\n')

num_1 = int(input('Inserte el primer valor: \n'))
num_2 = int(input('Inserte el segundo valor: \n'))
num_3 = int(input('Inserte el tercer valor: \n'))

suma_valores = num_1+num_2+num_3

if num_1 == num_2 == num_3:
    print(suma_valores*3)
else:
    print(suma_valores)
