class Carro:

    # Atributos de clase
    # Lo que le atribuye al carro
    color = "rojo"
    kms = 60
    price = 10000
    velocidad = 0

    # Métodos de clase
    # Lo que hace el carro
    def acelerar(self):
        self.velocidad += 1
        return 'Estoy acelerando por uno'

    def frenar(self):
        return 'Estoy frenando'

    def girar(self):
        return 'Estoy girando'

    # Constructor
    def __init__(self, color, kms, price):
        self.color = color
        self.kms = kms
        self.price = price


blue_car = Carro("azul", 100, 20000)
print(blue_car.velocidad)
print(blue_car.acelerar())
print(blue_car.velocidad)
