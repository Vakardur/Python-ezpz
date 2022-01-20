from site import venv
from .models import Articulo


# EN ESTE ARCHIVO VA TODA LA LOGICA DE LA APLICACION

def initialize_new_article():
    articulo = Articulo('', 0.0, 0)
    print(articulo)
    return articulo


def vender_pan(pan):
    pan.stock -= 1
    return pan
