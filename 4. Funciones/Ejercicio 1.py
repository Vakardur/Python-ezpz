"""Haga una función que multiplique dos números y devuelva el cuadrado de ese resultado. 
Replique la función utilizando Lambda."""

#Función normal

num1 = int(input('Ingrese el primer número:\n'))
num2 = int(input('Ingrese el segundo número:\n'))

def sqrd_mult(x,y):
    mult = x*y
    exponent = mult**2
    return exponent

print('El resultado es',sqrd_mult(num1,num2))

#Función Lambda
print('La función lambda regresa:')
sq_mult2 = lambda x,y:(x*y)**2

print(sq_mult2(num1,num2))