# EN ESTE ARCHIVO VA TODA LA LOGICA DE LOS DATOS

class Articulo:

    name: str = ''
    price: float = 0.0
    stock: int = 0

    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock


class Venta:

    comprador: str = ''
    articulo: Articulo = Articulo('', 0.0, 0)
    cantidad: int = 0

    def __init__(self, comprador: str, articulo: Articulo, cantidad: int):
        self.comprador = comprador
        self.articulo = articulo
        self.cantidad = cantidad
