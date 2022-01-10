"""Escribe un programa para separar números positivos y negativos de la lista.
"""

lista = [302, -987, -979, 930, -118, 760, 11, -866, -251, 256, 724, -706, -661, 588, -179, 837, 340, 243, -909, 484, -172, -180, -248, 836, -194, 163, -289, -115, 912, 487, -282, -940, -142, 439, 174, -65, 840, 293, -169, 58, -357, -296, 729, 762, -479, 930, 804, 470, -298, 686, 637, -984, 108, -461, 977, 298, 839, -895, 319, 749, -971, -374, 281, -433, -356, 554, -874, 596, 565, 714]

LISTA_POSITIVOS = []
LISTA_NEGATIVOS = []

#for

for x in lista:
    if x >= 1:
        LISTA_POSITIVOS.append(x)
    else:
        LISTA_NEGATIVOS.append(x)


print(LISTA_NEGATIVOS)
print(LISTA_POSITIVOS)

#While

LISTA_NEGATIVOS2 = []
LISTA_POSITIVOS2 = []

while lista:
    num = lista.pop(0) 
    if num >= 1: 
        LISTA_POSITIVOS2.append(num)
    else:
        LISTA_NEGATIVOS2.append(num)

print(LISTA_NEGATIVOS2)
print(LISTA_POSITIVOS2)

 