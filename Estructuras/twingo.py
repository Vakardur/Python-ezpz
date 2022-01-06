import random
import math


class Twingo:
    nickname: str = None
    velocidad = 0
    posicion = 0
    degradacion = 0

    def acelerar(self):
        accel = random.randint(0, 20)
        if self.velocidad + accel > 40:
            reduced_accel = ((self.velocidad + accel) / 2)
            self.velocidad = math.ceil(reduced_accel)
            self.degradacion += 1
        else:
            self.velocidad += accel
        self.posicion += self.velocidad

    def __init__(self, nickname):
        self.nickname = nickname


racers = [Twingo("Cardenas"), Twingo("Alejo"), Twingo("Joshua")]

timer = 0
time_limit = 20

while timer <= time_limit:
    for racer in racers:
        racer.acelerar()
    timer += 1

posiciones = [[racer.nickname, racer.posicion] for racer in racers]
velocidad = [[racer.nickname, racer.velocidad] for racer in racers]
degradacion = [[racer.nickname, racer.degradacion] for racer in racers]

# this is just to speed things up and introduce lambda.
# ordinarily, one would need to create a list with the values of each
# and get the max value of each.
print(max(posiciones, key=lambda x: x[1]))
print(max(velocidad, key=lambda x: x[1]))
print(max(degradacion, key=lambda x: x[1]))
