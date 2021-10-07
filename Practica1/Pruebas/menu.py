import tkinter as tk
from tkinter import Image, filedialog, Label
import os
from PIL import Image
from operaciones import *



def abrirImagen():
    ruta = str(os.path.dirname(os.path.abspath(__file__)))
    rutaImagen = str(filedialog.askopenfilename(initialdir = ruta,title = "Abrir imagen",filetypes = (("Imagenes","*.jpg;*.png"),("All files","*.*"))))
    imagen = Image.open(rutaImagen, 'r')
    imagen.show()
    col, row = imagen.size
    datos = list(imagen.getdata())

    matrizR = MatrizColor(row, col)
    matrizG = MatrizColor(row, col)
    matrizB = MatrizColor(row, col)
    matrizEscalaGrises = MatrizColor(row, col)

    cont = 0
    k = 0

    for i in range(row):
        if i != row:
            while (cont < col):
                matrizR.setVal(i, cont, int(datos[k][0]))
                matrizG.setVal(i, cont, int(datos[k][1]))
                matrizB.setVal(i, cont, int(datos[k][2]))
                # Codificación escala de grises PAL
                matrizEscalaGrises.setVal(i, cont, ((0.222 * int(datos[k][0])+ (0.707 * int(datos[k][1])) + (0.071 * int(datos[k][2])))))
                cont += 1
                k += 1
            cont = 0

    print(f'EL brillo de R es: {brillo(matrizR, row, col)}')

 
def guardar():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))

def guardarComo():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))


def main():

    def salir():
        app.quit()

    app = tk.Tk()

    app.geometry('800x700')
    app['bg']='#58F49A'
    app.title("Prueba Visión por Computador")

    barraMenu = tk.Menu(app)

    # Menu del archivo
    menuArchivo = tk.Menu(barraMenu)
    menuArchivo.add_command(label="Abrir imagen", command=abrirImagen)
    menuArchivo.add_command(label="Guardar", command=guardar)
    menuArchivo.add_command(label="Guardar como", command=guardarComo)
    menuArchivo.add_command(label="Salir", command=salir)
    barraMenu.add_cascade(label="Archivo", menu=menuArchivo)

    # Menu de herramienta
    menuHerramientas = tk.Menu(barraMenu)
    menuHerramientas.add_command(label="Abrir imagen", command=abrirImagen)
    menuHerramientas.add_command(label="Guardar", command=guardar)
    menuHerramientas.add_command(label="Guardar como", command=guardarComo)
    menuHerramientas.add_command(label="Salir", command=salir)

    barraMenu.add_cascade(label="Herramientas", menu=menuHerramientas)

    app.config(menu=barraMenu)

    label = Label(text="F O T O C H O P")
    label.pack()
    label.config(fg="black", bg="#58F49A", font=("Verdana", 24))

    app.mainloop()

main()