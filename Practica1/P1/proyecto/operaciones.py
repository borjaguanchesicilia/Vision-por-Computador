import tkinter as tk
from tkinter import Label, Image, filedialog, messagebox
import os
from tkinter.constants import END
from typing import Tuple
import numpy as np
from PIL import Image, ImageTk
from matplotlib.pyplot import bar, hist
from functools import partial
from numpy.core.numeric import indices
from math import pow, sqrt, log2
import matplotlib.pyplot as plt
from matriz import *


app = tk.Tk(); barraMenu = tk.Menu(app); etiquetaTam = tk.Label()
borrar = 0
listaImagenes = []; indiceIm = 0


def fEtiquetaTam():
    global etiquetaTam
    etiquetaTam.destroy()
    etiquetaTam = tk.Label(app,text =f'{listaImagenes[indiceIm][1]} x {listaImagenes[indiceIm][2]} px')
    etiquetaTam.place(relx = 0.0, rely = 1.0, anchor ='sw')


def fMenuHistorial(borrarHistorial=1):

    if (borrarHistorial == 1):
        barraMenu.delete(END)
    
    menuHistorial = tk.Menu(barraMenu)
    for i in range(len(listaImagenes)):
        menuHistorial.add_command(label=str(listaImagenes[i][0]), command= partial(reabrirImagen, i))
    
    barraMenu.add_cascade(label="Historial", menu=menuHistorial)


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


def calcularHistograma(matriz, filas, columnas):

    vectorHistograma = []

    [vectorHistograma.append(0) for i in range(256)]

    for i in range(filas):
        for j in range(columnas):
            vectorHistograma[matriz.getVal(i, j)] += 1

    return vectorHistograma


def graficarHistograma(frecuencias, nombre):
    colores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255]
    plt.figure(nombre)
    plt.title("Histograma de la imagen " + nombre)
    plt.xlabel("Colores")
    plt.ylabel("Frecuencias")
    plt.bar(colores, frecuencias, width=1.2)
    plt.show()


def calcularBrillo(histograma, filas, columnas):
    n = filas*columnas
    sum = 0
    media = 0
    for i in range(len(histograma)):
        sum += i*histograma[i]
    
    media = sum / n

    return round(media)


def calcularContraste(histograma, filas, columnas, media):
    n = filas*columnas
    sum = 0
    desviacion = 0
    for i in range(len(histograma)):
        sum += histograma[i] * pow((i - media), 2)
    
    desviacion = sqrt(sum / n)

    return round(desviacion)


def calcularEntropia(histograma, filas, columnas):

    n = filas*columnas; sum = 0; entropia = 0; probI = 0

    for i in range(len(histograma)):
        probI = histograma[i] / n
        if (probI != 0.0):
            sum += probI * log2(probI)
    
    entropia = -sum

    return entropia


def calcularNegativo():

    global indiceIm; 

    negativo = [255, 254, 253, 252, 251, 250, 249, 248, 247, 246, 245, 244, 243, 242, 241, 240, 239, 238, 237, 236, 235, 234, 233, 232, 231, 230, 229, 228, 227, 226, 225, 224, 223, 222, 221, 220, 219, 218, 217, 216, 215, 214, 213, 212, 211, 210, 209, 208, 207, 206, 205, 204, 203, 202, 201, 200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181, 180, 179, 178, 177, 176, 175, 174, 173, 172, 171, 170, 169, 168, 167, 166, 165, 164, 163, 162, 161, 160, 159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144, 143, 142, 141, 140, 139, 138, 137, 136, 135, 134, 133, 132, 131, 130, 129, 128, 127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    matrizR = Matriz(0, 0); matrizG = Matriz(0, 0); matrizB = Matriz(0, 0); matrizEscalaGrises = Matriz(0, 0)
    matrizR.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizG.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizB.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizEscalaGrises.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])

    cont = 0; listaAux = []; pixels = []

    for i in range(listaImagenes[indiceIm][1]):
        if i != listaImagenes[indiceIm][1]:
            while (cont < listaImagenes[indiceIm][2]):
                r = negativo[listaImagenes[indiceIm][4].getVal(i, cont)]
                g = negativo[listaImagenes[indiceIm][5].getVal(i, cont)]
                b = negativo[listaImagenes[indiceIm][6].getVal(i, cont)]
                listaAux.append((r, g, b))
                matrizR.setVal(i, cont, r)
                matrizG.setVal(i, cont, g)
                matrizB.setVal(i, cont, b)

                # Codificación escala de grises PAL
                matrizEscalaGrises.setVal(i, cont, (round(0.222 * r) + round(0.707 * g) + round(0.071 * b)))
                
                cont += 1
            pixels.append(listaAux)
            cont = 0
            listaAux = []

    array = np.array(pixels, dtype=np.uint8)
    new_image = Image.fromarray(array)
    nombre = "./backupImagenes/"+listaImagenes[indiceIm][0][:-4]+"Negativo.jpg"
    new_image.save(nombre)

    listaImagenes.insert(0, [str(listaImagenes[indiceIm][0][:-4]+"Negativo.jpg"), listaImagenes[indiceIm][1], listaImagenes[indiceIm][2], matrizEscalaGrises, matrizR, matrizG, matrizB, [], 0, 0, 0])
    fMenuHistorial()
    
    return nombre