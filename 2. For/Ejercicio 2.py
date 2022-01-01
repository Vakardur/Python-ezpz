"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad). 
E.g. tengo 4 entonces se imprime 1 2 3 4"""

#Definimos la entrada de usuario como una variable 'edad', que es un input de un integer. 
edad = int(input('¿Cuántos años tiene?\n'))

# Estructuramos el For. Edad debe ser el rango, pero como range() inicia desde 0, hay que asignar parámetro de inicio como 1. Para incluir el número 
# final del rango, el stop del range() debe ser edad+1. 
for n in range(1,edad+1):
    #Para cada iteración, el programa imprime el valor de n incrementando en el rango anterior.
    print(n)