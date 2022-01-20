"""
    Graphical User Interface.
Tkinter is a Python module that provides a simple GUI.
Tkinter > JavaScript->React > C++ > Unity
"""

# EN ESTE ARCHIVO SOLO VAN COSAS RELACIONADAS A LA INTERFAZ GRAFICA

from tkinter import Button, Entry, Tk, Label
import tkinter.font as font


# Init
root = Tk(className="Tiendita de la esquina")

root.geometry("500x500")
root.resizable(False, False)
root.configure(background="white")
# root.iconbitmap('icon.ico') dentro de la carpeta de GUI


# font config
arial = font.Font(family="Arial", size=20)


# title
title = Label(root, text="Tiendita de la esquina", background="white")
title['font'] = arial
title.pack()


# button
# command es lo que ejecutará el botón al darle click
button = Button(root, text="Click me", background="white",
                command=lambda x: print('hola'), width=20, height=10)
button['font'] = arial

# entry
data_entry = Entry(root, width=20, background="#f9a9f9")
button.pack()
data_entry.pack()

root.bind('<space>', lambda x: print('hola con espacio'))

if __name__ == "__main__":
    root.mainloop()


"""
VENDA UN ARTICULO

Ponga un botón con una imagen adentro de un pan. Si le doy click al pan aparece una entrada de texto y un botón de confirmar.

Si le doy click a confirmar, por consola imprima el nuevo stock del artículo.
Empiece con:
pancito = Articulo('pancito', 200.0, 10)


# if algo:
#     data_entry.pack()
"""
