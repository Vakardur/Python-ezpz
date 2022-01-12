"""Haga una función que tome un número y retorne la longitud de ese número 
(4104 tiene longitud de 4). Replique la función utilizando Lambda. """


#función normal
numero = (input('Ingrese un número:\n'))

def longitud(x):
    return len(x)

print('El número tiene', longitud(numero),'dígitos.\n')

#Función lambda
print('La función lambda dice:')
numlength = lambda x: len(x)
print('El número tiene',numlength(numero),'dígitos.')