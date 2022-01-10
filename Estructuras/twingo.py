import random
import math


class Twingo:
    nickname: str = None
    velocidad = 0
    posicion = 0
    degradacion = 0
    pits_arrivals = 0
    is_in_pits = 0

    def acelerar(self):
        accel = random.randint(0, 20)
        if self.velocidad + accel > 40:
            reduced_accel = ((self.velocidad + accel) / 2)
            self.velocidad = math.ceil(reduced_accel)
            self.degradacion += 1
            if self.degradacion % 4 == 0:
                self.pits_arrivals += 1
                self.is_in_pits += 2
        else:
            self.velocidad += accel
        self.posicion += self.velocidad

    def waits_at_pits(self):
        self.is_in_pits -= 1

    def __init__(self, nickname):
        self.nickname = nickname


racers = [Twingo("Cardenas"), Twingo("Alejo"), Twingo("Joshua")]

timer = 0
time_limit = 20

while timer <= time_limit:
    for racer in racers:
        if racer.is_in_pits > 0:
            racer.waits_at_pits()
        else:
            racer.acelerar()
    timer += 1

posiciones = [[racer.nickname, racer.posicion] for racer in racers]
velocidad = [[racer.nickname, racer.velocidad] for racer in racers]
degradacion = [[racer.nickname, racer.degradacion] for racer in racers]
pits_arrivals = [[racer.nickname, racer.pits_arrivals] for racer in racers]


winner = ['', 0]
for racer in racers:
    if racer.posicion > winner[1]:
        winner = [racer.nickname, racer.posicion]

max_vel = ['', 0]
for racer in racers:
    if racer.velocidad > max_vel[1]:
        max_vel = [racer.nickname, racer.velocidad]

degraded_car = ['', 0]
for racer in racers:
    if racer.degradacion > degraded_car[1]:
        degraded_car = [racer.nickname, racer.degradacion]

pitted_car = ['', 0]
for racer in racers:
    if racer.pits_arrivals > pitted_car[1]:
        pitted_car = [racer.nickname, racer.pits_arrivals]

print('----------normal way ----------')
print('winner', winner)
print('max_vel', max_vel)
print('degraded_car', degraded_car)
print('pitted_car', pitted_car)


# this is just to speed things up and introduce lambda.
# ordinarily, one would need to create a list with the values of each
# and get the max value of each.
print('\n ---------- lambda way ----------')
print('ganador: ', max(posiciones, key=lambda x: x[1]))
print('velocidad max: ', max(velocidad, key=lambda x: x[1]))
print('carro mas cascado: ', max(degradacion, key=lambda x: x[1]))
print('carro mas pitteado: ', max(pits_arrivals, key=lambda x: x[1]))
