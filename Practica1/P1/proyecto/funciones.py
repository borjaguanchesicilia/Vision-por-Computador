import tkinter as tk
from tkinter import Label, Image, filedialog, messagebox
import os
from tkinter.constants import END
import numpy as np
from PIL import Image, ImageTk
from matplotlib.pyplot import bar, hist
from functools import partial
from numpy.core.numeric import indices
from operaciones import *

app = tk.Tk(); barraMenu = tk.Menu(app); etiquetaTam = tk.Label()
flag = 0
listaImagenes = []; indiceIm = 0


def abrirImagen():
    global flag; global listaImagenes; global indiceIm
    nombreImagen = ""; filas = 0; columnas = 0
    matrizEscalaGrises = Matriz(0, 0)
    histograma = []; brillo = 0; contraste = 0; entropia = 0
    
    ruta = str(os.path.dirname(os.path.abspath(__file__)))
    rutaImagen = str(filedialog.askopenfilename(initialdir = ruta,title = "Abrir imagen",filetypes = (("Imagenes","*.jpg;*.png"),("All files","*.*"))))
    imagen = Image.open(rutaImagen, 'r')
    #imagen.show()
    nombreImagen = rutaImagen[::-1]
    index = 0	
    for i in range(len(nombreImagen)):
        if (nombreImagen[i] == "/"):
            index = i
            break

    nombreImagen = nombreImagen[0:index][::-1]

    columnas, filas = imagen.size
    datos = list(imagen.getdata())

    # Redimensionar matriz escala grises
    matrizEscalaGrises.actualizar(filas, columnas)

    # Mostrar imagen + imagen blanco
    imagen1(nombreImagen); imagen2("blanco.png")

    cont = 0; k = 0

    for i in range(filas):
        if i != filas:
            while (cont < columnas):
                # Codificación escala de grises PAL
                matrizEscalaGrises.setVal(i, cont, (round(0.222 * int(datos[k][0]) + round(0.707 * int(datos[k][1]))) + round(0.071 * int(datos[k][2]))))
                cont += 1; k += 1
            cont = 0

    listaImagenes.append([nombreImagen, filas, columnas, matrizEscalaGrises, histograma, brillo, contraste, entropia])
    indiceIm = len(listaImagenes) - 1
    fEtiquetaTam()

    cont = 0; listaAux = []; pixels = []

    for i in range(len(datos)):
        cont += 1
        if(cont != columnas):
            listaAux.append(datos[i])
        else:
            pixels.append(listaAux)
            cont = 0
            listaAux = []

    array = np.array(pixels, dtype=np.uint8)
    new_image = Image.fromarray(array)
    new_image.save('./backupImagenes/'+nombreImagen)
    
    # Menu de imagenes
    if (flag == 1):
        barraMenu.delete(END)
    
    flag = 1
    menuHistorial = tk.Menu(barraMenu)
    for i in range(len(listaImagenes)):
        menuHistorial.add_command(label=str(listaImagenes[i][0]), command= partial(reabrirImagen, i))
    
    barraMenu.add_cascade(label="Historial", menu=menuHistorial)



def reabrirImagen(val):
    # Indice de la imagen con la que se trabaja actualmente
    global indiceIm; indiceIm = val
    
    imagen1("./backupImagenes/"+listaImagenes[indiceIm][0])
    fEtiquetaTam()


def guardar():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))


def guardarComo():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))


def fError():
   messagebox.showerror("ERROR", "Debe de abrir una imagen")


def fHistograma():

    if (listaImagenes[indiceIm][3].getFilas() != 0):
        if(len(listaImagenes[indiceIm][4]) == 0): # No se ha calculado el histograma
            listaImagenes[indiceIm][4] = calcularHistograma(listaImagenes[indiceIm][3], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
        graficarHistograma(listaImagenes[indiceIm][4], listaImagenes[indiceIm][0])
    else:
        fError()


def fBrillo():

    if (listaImagenes[indiceIm][3].getFilas() != 0):
        if (listaImagenes[indiceIm][5] == 0):
            if (len(listaImagenes[indiceIm][4]) == 0):
                listaImagenes[indiceIm][4] = calcularHistograma(listaImagenes[indiceIm][3], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
            listaImagenes[indiceIm][5] = calcularBrillo(listaImagenes[indiceIm][4], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
        messagebox.showinfo(title="Brillo", message=f"El brillo es: {str(listaImagenes[indiceIm][5])}")
    else:
        fError()


def fContraste():

    if (listaImagenes[indiceIm][3].getFilas() != 0):
        if (listaImagenes[indiceIm][6] == 0):
            if (listaImagenes[indiceIm][5] == 0):
                if (len(listaImagenes[indiceIm][4]) == 0):
                    listaImagenes[indiceIm][4] = calcularHistograma(listaImagenes[indiceIm][3], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
                listaImagenes[indiceIm][5] = calcularBrillo(listaImagenes[indiceIm][4], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
            listaImagenes[indiceIm][6] = calcularContraste(listaImagenes[indiceIm][4], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2], listaImagenes[indiceIm][5])
        messagebox.showinfo(title="Contraste", message=f"El contraste es: {str(listaImagenes[indiceIm][6])}")
    else:
        fError()


def fEntropia():

    if (listaImagenes[indiceIm][3].getFilas() != 0):
        if (listaImagenes[indiceIm][7] == 0):
            if (len(listaImagenes[indiceIm][4]) == 0):
                listaImagenes[indiceIm][4] = calcularHistograma(listaImagenes[indiceIm][3], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
            listaImagenes[indiceIm][7] = calcularEntropia(listaImagenes[indiceIm][4], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
        messagebox.showinfo(title="Entropía", message=f"La entropía es: {str(listaImagenes[indiceIm][7])}")
    else:
        fError()


def fEtiquetaTam():
    global etiquetaTam
    etiquetaTam.destroy()
    etiquetaTam = tk.Label(app,text =f'{listaImagenes[indiceIm][1]} x {listaImagenes[indiceIm][2]} px')
    etiquetaTam.place(relx = 0.0, rely = 1.0, anchor ='sw')


def imagen1(nombre):

    im = ImageTk.PhotoImage(Image.open(nombre).resize((390,265)))
    imagen1 = tk.Label(image=im)
    imagen1.image = im
    imagen1.place(x=90, y=90)


def imagen2(nombre):

    im2 = ImageTk.PhotoImage(Image.open(nombre).resize((390,265)))
    imagen2 = tk.Label(image=im2)
    imagen2.image = im2
    imagen2.place(x=800, y=90)