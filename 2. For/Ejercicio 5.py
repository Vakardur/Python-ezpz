#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

primo = int(input("Escriba un número entero:\n"))

if primo > 1:
    for x in range(2,primo):
        if(primo % x) == 0:
            print(primo,"no es un número primo")
            break
    else:
        print(primo,"es un número primo.")
else:
    print(primo, "no es un número primo.")