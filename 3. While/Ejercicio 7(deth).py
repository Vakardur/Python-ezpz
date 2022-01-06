"""
a. Cree una clase Twingo. Defina sus atributos y métodos.
    i.Los atributos deben ser nickname, velocidad (que siempre debe ser cero al principio), posición (que siempre debe ser 0 al principio), y 
        degradación (que siempre debe ser cero al principio)
    ii. Uno de los métodos debe llamarse acelerar() y debe devolver un valor aleatorio de 0 a 20.
    iii. Acelerar() debe sumarle su valor a la velocidad del Twingo.
b. Defina tres Twingos.
c. Declare una variable llamada tiempo. 
d. En un loop, instancie una carrera, siguiendo las siguientes reglas:
    i.En cada iteración, cada Twingo llama su método acelerar(). El resultado se debe sumar a la velocidad.
    ii. El valor nuevo de la aceleración debe sumarse al atributo de posición del Twingo.
    iii. Cada que el tiempo sea múltiplo de 7, habrá un bache en el camino. Aquellos que, luego de acelerar, tengan una velocidad de 40, 
    tendrán que dividir su velocidad resultante por dos antes de sumar la nueva distancia. Por ejemplo, si un Twingo en un turno, 
    llama a acelerar(), y la suma de su velocidad anterior y la nueva es 42, entonces la distancia se dividirá en dos, resultando en 21. 
    Este 21 es el valor que debe ser agregado a la distancia recorrida. Cuando esto pase, también, el atributo de degradación de ese Twingo 
    debe subir por uno. Tenga cuidado con la división, si le da un decimal, tome el entero siguiente más alto (e.g., 3.5 es 4).
e. Al final del loop, cada Twingo tendrá su propio valor de velocidad, y su propia distancia.
    i. Imprima qué carro ganó. Es decir, el carro con mayor distancia.
    ii. Imprima qué carro iba más rápido al final (valor máximo de aceleración)
    iii. Imprima qué carro tuvo que frenar más veces para evitar dañar sus amortiguadores.
"""
import random

class Twingo:

    # Atributos
    nickname = ""
    velocidad = 0
    posición = 0
    degradación = 0

    # Métodos
    def acelerar(self):
        value = random.randrange(1,21,1)
        self.posición = self.posición + value

    def __init__(self, nickname, velocidad, posición, degradación):
        self.nickname = nickname
        self.velocidad = velocidad
        self.posición = posición
        self.degradación = degradación

Twingo1= Twingo("Twingod",0,0,0)
Twingo2 = Twingo("Merchopercho",0,0,0)

print("Twingódromo de Gachancipá.\n")
print("Los competidores de hoy son",Twingo1.nickname, "vs.", Twingo2.nickname)


#Piques
for speed in range(1,100):
    Twingo1.acelerar()
    Twingo2.acelerar()
