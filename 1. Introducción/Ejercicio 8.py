#Escriba un programa en Python para convertir la altura (en pies y pulgadas) a centímetros.

#Datos importantes:
#1cm = 0,3937 in.

print('America units to actually useful units calculator (in a console edition)\n')

pies = int(input("Pies: \n"))
pulgadas = int(input("Pulgadas\n"))

pulgadas += pies*12
centímetros = round(pulgadas*2.54, 1)

print("Su altura es %d cm." %centímetros)