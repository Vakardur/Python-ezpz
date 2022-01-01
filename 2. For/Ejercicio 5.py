"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""

#Definimos la entrada de usuario como una variable "primo" siendo un input de un integer.
primo = int(input("Escriba un número entero:\n"))

#Un número primo es un número natural mayor que 1 que sólamente tiene dos divisores positivos; él mismo y 1. Así, hay que implementar una validación
#con estos criterios. La primera: tiene que ser mayor que 1...
if primo > 1:
    #Si el número es mayor que 1, se pasa a la primera validación. Como el 1 no se considera primo, el rango a validar arranca desde el número 2 y va
    #hasta el número a probar "primo"
    for x in range(2,primo):
        #Segunda validación; si el remanente del número dividido por los valores de X es igual a 0...
        if(primo % x == 0):
            #... se imprime que el número no es primo...
            print(primo,"no es un número primo.")
            #... y se genera un break para detener el programa.
            break
    #Si el programa cumple con las condiciones hasta ahora, se imprime que el valor sí es un número primo. 
    else:
        print(primo,"es un número primo.")
else:
    print(primo, "no es un número primo.")