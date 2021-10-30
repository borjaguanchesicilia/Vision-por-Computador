import tkinter as tk
import time
from tkinter.constants import ANCHOR, END

app = tk.Tk()
lista = tk.Listbox(app)
lista.pack(pady=15)

def eliminar():
    lista.delete(ANCHOR)

def seleccionar():
    print("hola")

for i in range(5):
    lista.insert(END, "imagen "+str(i))

botonEliminar = tk.Button(app, text="Eliminar", command=eliminar)
botonEliminar.pack(pady=10)


botonSeleccionar = tk.Button(app, text="Seleccionar", command=seleccionar)
botonSeleccionar.pack(pady=10)

app.mainloop()