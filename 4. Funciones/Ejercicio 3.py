"""Haga tres funciones que cumplan con los siguientes parámetros. Replique cada función utilizando Lambda.
a. Una función que tome un texto, y le devuelva todos los caracteres en mayúscula.
b. Una función que tome un texto, y le devuelva todos los caracteres en minúscula.
c. Una función que tome un texto, y le agregue al texto su longitud (por ejemplo, arroz se transformaría en arroz5).
"""

text = input('Escriba una palabra:\n')
#Función mayúscula normal
def mayus(x):
    return x.upper()

print('Tu palabra','"',text,'"','ahora se lee\n',mayus(text))
#Función mayúscula lambda

l_mayus = lambda x: x.upper()
print('Lambda imprime:',l_mayus(text))
#Función minúscula normal

def minus(x):
    return x.lower()

print('Tu palabra','"',text,'"','ahora se lee\n',minus(text))

#Función minúscula lambda
l_minus = lambda x: x.lower()
print('Lambda imprime:',l_minus(text))

#función longitud normal

def wordlen(x):
    numlen = str(len(x))
    return x + numlen

print(wordlen(text))

#Función longitud lambda
lamlen = lambda x: x + str(len(x))
print('Lambda imprime:', lamlen(text))