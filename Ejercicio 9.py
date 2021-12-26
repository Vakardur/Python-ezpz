# Escriba un programa en Python para convertir segundos en días.
print('Second to day converter. Ft. Farruko')

segundos = int(input('Cuántos segundos han pasado?\n'))

día = round(segundos / 86400, 2)

if día == 1:
    print('Eso es', día, 'día.')
else:
    print('Eso son', día, 'días.')
