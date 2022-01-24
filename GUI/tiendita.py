# Aqui va la lógica de la tienda
"""
    Graphical User Interface.
Tkinter is a Python module that provides a simple GUI.
Tkinter > JavaScript->React > C++ > Unity
"""

# EN ESTE ARCHIVO SOLO VAN COSAS RELACIONADAS A LA INTERFAZ GRAFICA

from tkinter import Tk, Label, Entry, Button, PhotoImage, StringVar
import tkinter.font as font
from models import Articulo


# Init
root = Tk(className="Tiendita de la esquina")

root.geometry("500x500")
root.resizable(False, False)
root.configure(background="white")
# root.iconbitmap('icon.ico') dentro de la carpeta de GUI

# font config
arial = font.Font(family="Arial", size=20)
pancitoNumber = StringVar()

# title
title = Label(root, text="Tiendita de la esquina", background="white")
title['font'] = arial
title.pack()

pancito = Articulo('pancito', 200.0, 10)


def new_entry():
    new_entry = Entry(root, width=15, background='#f9a9f9',
                      textvariable=pancitoNumber)
    new_entry.pack()


def reduce_stock():
    pancito.stock -= int(pancitoNumber.get())
    print(pancito.stock)


def confirmbutton():
    newbtn = Button(root, command=reduce_stock, text='Confirm')
    newbtn.pack()
# button
# command es lo que ejecutará el botón al darle click


pan_img = PhotoImage(file=r'GUI\pan.png')
pan_btn = pan_img.subsample(10, 10)
SaleButton = Button(root, image=pan_btn,
                    command=lambda: [new_entry(), confirmbutton()], state=is_shown)
SaleButton['font'] = arial

# entry
data_entry = Entry(root, width=20, background="#f9a9f9")
SaleButton.pack()


root.bind('<space>', lambda x: print('hola con espacio'))

if __name__ == "__main__":
    root.mainloop()


"""
VENDA UN ARTICULO

Ponga un botón con una imagen adentro de un pan. Si le doy click al pan aparece 
una entrada de texto y un botón de confirmar.

Si le doy click a confirmar, por consola imprima el nuevo stock del artículo.
Empiece con:
pancito = Articulo('pancito', 200.0, 10)


# if algo:
#     data_entry.pack()
"""
