#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad). 
# E.g. tengo 4 entonces se imprime 1 2 3 4

edad = int(input('¿Cuántos años tiene?'))

for n in range(1,edad+1):
    print(n)