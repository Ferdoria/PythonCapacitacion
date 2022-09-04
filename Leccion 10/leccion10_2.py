# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables,
# también debe de tener un label con el texto que queráis.

from tkinter import *

windows = Tk()

label = Label(text="Lista de colores")
label.pack()

elemento = StringVar()
lista = Listbox(windows)

for item in ["Rojo", "Blanco", "Azul"]:
    lista.insert(END, item)
    lista.pack()

windows.mainloop()