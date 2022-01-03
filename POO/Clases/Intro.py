class Carro:

    # Atributos de clase
    # Lo que le atribuye al carro
    color = "rojo"
    kms = 60
    price = 10000

    # Métodos de clase
    # Lo que hace el carro
    def acelerar(self):
        return 'Estoy acelerando'

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
print(blue_car.acelerar())
