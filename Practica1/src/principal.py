from os import error
import tkinter as tk
from tkinter import Tk, Label, messagebox, Toplevel, Button
from tkinter.constants import END, W
from tkinter.ttk import *
from functools import partial
import matplotlib.pyplot as plt
from matriz import *
import numpy as np
from PIL import Image, ImageTk, ImageDraw
import shutil


app = tk.Tk(); barraMenu = tk.Menu(app); etiquetaTam = tk.Label(); bIntroducirTramo = Button(app, text ="Click para comprobar"); bComprobarTramos = Button(app, text ="Click para comprobar")
borrar = 0
listaImagenes = []; indiceIm = 0
listaPuntos = []; cont = 0
nuevosPixels = []
brilloAl = 0; contrasteAl = 0
valorGamma = 0
umbral = 0
valAl = 0; valTf = 0


def fCopiaImagen(nombre):

    filas = listaImagenes[indiceIm][1]; columnas = listaImagenes[indiceIm][2]

    matrizR = Matriz(0, 0); matrizG = Matriz(0, 0); matrizB = Matriz(0, 0); matrizEscalaGrises = Matriz(0, 0)
    matrizR.actualizar(filas, columnas); matrizG.actualizar(filas, columnas); matrizB.actualizar(filas, columnas); matrizEscalaGrises.actualizar(filas, columnas)

    j = 0; listaAux = []; pixels = []

    for i in range(filas):
        if i != filas:
            while (j < columnas):
                r = listaImagenes[indiceIm][4].getVal(i, j)
                g = listaImagenes[indiceIm][5].getVal(i, j)
                b = listaImagenes[indiceIm][6].getVal(i, j)
                listaAux.append((r, g, b))
                matrizR.setVal(i, j, r)
                matrizG.setVal(i, j, g)
                matrizB.setVal(i, j, b)

                # Codificación escala de grises PAL
                matrizEscalaGrises.setVal(i, j, (round(0.222 * r) + round(0.707 * g) + round(0.071 * b)))
                
                j += 1
            pixels.append(listaAux)
            j = 0
            listaAux = []

    array = np.array(pixels, dtype=np.uint8)
    new_image = Image.fromarray(array)
    nombre = './backupImagenes/'+listaImagenes[indiceIm][0][:-4]+"Copia.jpg"
    new_image.save(nombre)


def fMenuHistorial(borrarHistorial=1):

    if (borrarHistorial == 1):
        barraMenu.delete(END)
    
    menuHistorial = tk.Menu(barraMenu)
    for i in range(len(listaImagenes)):
        menuHistorial.add_command(label=str(listaImagenes[i][0]), command= partial(reabrirImagen, i))
    
    barraMenu.add_cascade(label="Historial", menu=menuHistorial)


def fEtiquetaTam(indice):
    global etiquetaTam
    etiquetaTam.destroy()
    etiquetaTam = tk.Label(app,text =f'{listaImagenes[indice][1]} x {listaImagenes[indice][2]} px')
    etiquetaTam.place(relx = 0.0, rely = 1.0, anchor ='sw')


def pintarCuadro1(nombre):

    im = ImageTk.PhotoImage(Image.open(nombre).resize((390,265)))
    imagen1 = tk.Label(image=im)
    imagen1.image = im
    imagen1.place(x=90, y=90)


def pintarCuadro2(nombre):

    im2 = ImageTk.PhotoImage(Image.open(nombre).resize((390,265)))
    imagen2 = tk.Label(image=im2)
    imagen2.image = im2
    imagen2.place(x=800, y=90)


def reabrirImagen(val):
    # Indice de la imagen con la que se trabaja actualmente
    global listaImagenes;
 
    listaImagenes[0], listaImagenes[val] = listaImagenes[val], listaImagenes[0]

    fMenuHistorial()
    
    pintarCuadro1('./backupImagenes/'+listaImagenes[indiceIm][0]); pintarCuadro2("./funciones/blanco.png")
    fEtiquetaTam(indiceIm)


def hide_widget(widget):
   widget.pack_forget()