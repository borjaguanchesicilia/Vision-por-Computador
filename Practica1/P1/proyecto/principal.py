from os import error
import tkinter as tk
from tkinter import Tk, Label, messagebox, Toplevel, Button
from tkinter.constants import END, W
from tkinter.ttk import *
from functools import partial
import matplotlib.pyplot as plt
from matriz import *
import numpy as np
from PIL import Image, ImageTk


app = tk.Tk(); barraMenu = tk.Menu(app); etiquetaTam = tk.Label(); bIntroducirTramo = Button(app, text ="Click para comprobar"); bComprobarTramos = Button(app, text ="Click para comprobar")
borrar = 0
listaImagenes = []; indiceIm = 0
listaPuntos = []; cont = 0
nuevosPixels = []
valorGamma = 0


def fMenuHistorial(borrarHistorial=1):

    if (borrarHistorial == 1):
        barraMenu.delete(END)
    
    menuHistorial = tk.Menu(barraMenu)
    for i in range(len(listaImagenes)):
        menuHistorial.add_command(label=str(listaImagenes[i][0]), command= partial(reabrirImagen, i))
    
    barraMenu.add_cascade(label="Historial", menu=menuHistorial)


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


def reabrirImagen(val):
    # Indice de la imagen con la que se trabaja actualmente
    global listaImagenes;
 
    listaImagenes[0], listaImagenes[val] = listaImagenes[val], listaImagenes[0]

    fMenuHistorial()
    
    imagen1("./backupImagenes/"+listaImagenes[indiceIm][0]); imagen2("blanco.png")
    fEtiquetaTam()


def hide_widget(widget):
   widget.pack_forget()