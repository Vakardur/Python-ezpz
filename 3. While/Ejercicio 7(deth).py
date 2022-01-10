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

g. TRABAJO ADICIONAL POR JUGARLE AL VERGAS: cuando un Twingo tenga una degradación que sea múltiplo de 4, deberá 
ingresar a los pits a que les cambien las llantas. Debe haber un nuevo atributo llamado pits_arrivals, que cuente cuántas veces esto ocurra.
Tenga en cuenta que cuando un Twingo entre a los pits, no se podrá mover durante dos iteraciones.
    i. Por ejemplo, si mi Twingo tuvo que frenar y llegó a una degradación de 4 en la iteración 7, entonces ingresará a los pits. 
    Su atributo pits_arrivals aumentará por uno, y en la iteración 8 y 9 no se podrá mover.
"""
import random
import math

class Twingo:

    # Atributos
    nickname = ""
    velocidad = 0
    posición = 0
    degradación = 0
    pits_arrivals = 0
    pits_wait = 0 

    # Métodos
    def acelerar(self):
        v_accel = random.randint(0, 20)
        if self.velocidad + v_accel > 40:
            reduced_accel = ((self.velocidad + v_accel) / 2)
            self.velocidad = math.ceil(reduced_accel)
            self.degradación += 1
        else: 
            self.velocidad += v_accel
        self.posición += self.velocidad
        
        #pits
        if self.degradación % 4 == 0:
            self.pits_arrivals += 1
            self.pits_wait = 2
    

    def __init__(self, nickname):
        self.nickname = nickname
     

racers = [Twingo("Twingod"), Twingo("Merchopercho"), Twingo("Twingo86")]

#Piques

timer = 0
time_limit = 20

while timer <= time_limit:
    for racer in racers:
        if racer.pits_wait != 0:
            racer.pits_wait -= 1
        else:
            racer.acelerar()  
    timer += 1

posiciones = [[racer.nickname, racer.posición] for racer in racers]
velocidad = [[racer.nickname, racer.velocidad] for racer in racers]
degradación = [[racer.nickname, racer.degradación] for racer in racers]


winner_pos = [] 
winner_spd = [] 
winner_deg = [] 

maxpos = 0
maxspd = 0
maxdec = 0

for place in posiciones:
    if place[1] > maxpos:
        maxpos = place[1]
        winner_pos = place
for speed in velocidad:
    if speed[1] > maxspd:
        maxspd = speed[1]
        winner_spd = speed
for decay in degradación:
    if decay[1] > maxdec:
        maxdec = decay[1]
        winner_deg = decay

print(winner_pos)
print(winner_spd)
print(winner_deg)
