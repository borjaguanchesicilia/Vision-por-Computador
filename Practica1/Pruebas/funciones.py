from tkinter import Image, filedialog, messagebox
import os
from PIL import Image
from operaciones import *

nombreImagen = ""
matrizR = Matriz(0, 0); matrizG = Matriz(0, 0); matrizB = Matriz(0, 0); matrizEscalaGrises = Matriz(0, 0)
filas = 0; columnas = 0; histograma = []; brillo = 0

def abrirImagen():
    global nombreImagen
    global columnas
    global filas
    global matrizR
    global matrizG
    global matrizB
    global matrizEscalaGrises

    ruta = str(os.path.dirname(os.path.abspath(__file__)))
    rutaImagen = str(filedialog.askopenfilename(initialdir = ruta,title = "Abrir imagen",filetypes = (("Imagenes","*.jpg;*.png"),("All files","*.*"))))
    imagen = Image.open(rutaImagen, 'r')
    imagen.show()
    nombreImagen = rutaImagen[::-1]
    index = 0	
    for i in range(len(nombreImagen)):
        if (nombreImagen[i] == "/"):
            index = i
            break
        
    nombreImagen = nombreImagen[0:index][::-1]
    #imagen = Image.open("./benijo.jpg", 'r')

    columnas, filas = imagen.size
    datos = list(imagen.getdata())

    matrizR.actualizar(filas, columnas)
    matrizG.actualizar(filas, columnas)
    matrizB.actualizar(filas, columnas)
    matrizEscalaGrises.actualizar(filas, columnas)

    cont = 0
    k = 0

    for i in range(filas):
        if i != filas:
            while (cont < columnas):
                matrizR.setVal(i, cont, int(datos[k][0]))
                matrizG.setVal(i, cont, int(datos[k][1]))
                matrizB.setVal(i, cont, int(datos[k][2]))

                # Codificación escala de grises PAL
                matrizEscalaGrises.setVal(i, cont, (round(0.222 * int(datos[k][0]) + round(0.707 * int(datos[k][1]))) + round(0.071 * int(datos[k][2]))))
                cont += 1
                k += 1
            cont = 0
    

def guardar():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))


def guardarComo():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))


def fError():
   messagebox.showerror("ERROR", "Debe de abrir una imagen")


def fHistograma():
    global histograma

    if (matrizEscalaGrises.getFilas() != 0):
        histograma = calcularHistograma(matrizEscalaGrises, filas, columnas)
        graficarHistograma(histograma, nombreImagen)
    else:
        fError()


def fBrillo():
    global brillo

    if (matrizEscalaGrises.getFilas() != 0):
        brillo = calcularBrillo(histograma, filas, columnas)
        messagebox.showinfo(title="Brillo", message=f"El brillo es: {str(brillo)}")
    else:
        fError()


def fContraste():
    if (matrizEscalaGrises.getFilas() != 0):
        contraste = calcularContraste(histograma, filas, columnas, brillo)
        messagebox.showinfo(title="Contraste", message=f"El contraste es: {str(contraste)}")
    else:
        fError()