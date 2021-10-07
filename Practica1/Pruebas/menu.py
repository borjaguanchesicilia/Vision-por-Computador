import tkinter as tk
from tkinter import Image, filedialog, Label
import os
from PIL import Image
from matriz import *



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

    cont = 0
    i = 0

    print(datos[456])

    f = open("fichero.txt", "w")
    g = open("fichero2.txt", "w")
    g.write(str(datos))
    k = 0
    for i in range(row):
        if i != row:
            while (cont < col):
                #print(i, cont)
                #f.write(str(datos[k][0]) + "\n")
                #f.write(str(datos[k][0]) + "  " + str(datos[k][1]) + "  " + str(datos[k][2]) + "\n")
                matrizR.setVal(i, cont, int(datos[k][0])); matrizG.setVal(i, cont, int(datos[k][1])); matrizB.setVal(i, cont, int(datos[k][2]))
                cont += 1
                k += 1
            i += 1
            cont = 0
        f.write("\n\n")

    matrizG.mostrar()
        

    """matrizR = []
    matrizG = []
    matrizB = []
    matrizDatos = []
    arrayColores = []
    array = []

    for i in range(row):
        for j in range(col):
            array.append(0); arrayColores.append(0)
        matrizR.append(arrayColores)
        matrizG.append(arrayColores)
        matrizB.append(arrayColores)
        matrizDatos.append(array)
        array = []; arrayColores = []

    
    print("El tamaño de las matrices de colores es: ", len(matrizR), len(matrizR[4]))

    i = 0; j = 0

    for k in range(len(datos)):
        if (j != col-1):
            matrizDatos[i][j] = datos[k]
            j += 1
        else:
            i += 1
            j = 0

    print(matrizDatos[4][4][0], matrizDatos[4][4][1], matrizDatos[4][4][2])
    print(matrizR[0][829], matrizG[0][829])
    i = 0; j = 0

    for i in range(row):
        for j in range(col):
            matrizR[i][j] = matrizDatos[i][j][0]
            matrizG[i][j] = matrizDatos[i][j][1]
            matrizB[i][j] = matrizDatos[i][j][2]
            print(i, j)

    print("OK")"""


 
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

    label = Label(text="Herramienta para el procesamiento de imágenes")
    label.pack()
    label.config(fg="black", bg="#58F49A", font=("Verdana", 24))

    app.mainloop()

main()