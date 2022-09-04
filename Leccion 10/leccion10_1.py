#En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado
# y que contenga un botón de reinicio para que deje todo como al principio
#  Al principio no tiene que haber una opción seleccionada.

from tkinter import *

def seleccionar():
    mostrar.config(text="{}".format(opcion.get()))

def Limpiar():
    opcion.set(None)
    mostrar.config(text="")

windows = Tk()
opcion = StringVar()
opcion.set(None)

Radiobutton(windows, text = "Rojo", variable = opcion, value = 'Rojo', command = seleccionar).pack(anchor="w")
Radiobutton(windows, text = "Blanco", variable = opcion, value = 'Blanco', command = seleccionar).pack(anchor="w")
Radiobutton(windows, text = "Azul", variable = opcion, value = 'Azul', command = seleccionar).pack(anchor="w")

mostrar = Label(windows)
mostrar.pack()
Button(windows, text="Limpiar", command=Limpiar).pack()

windows.mainloop()