from collections import defaultdict
import pprint
from tkinter import filedialog

import numpy
from principal import *
import os


def fErrorDif():
   messagebox.showerror("ERROR", "Las imagenes deben ser del mismo tamaño")


def abrirImagenesDiferencia(imagen, tam):

    global listaImagenes; global indiceIm
    nombreImagen = ""; filas = 0; columnas = 0
    matrizR = Matriz(0, 0); matrizG = Matriz(0, 0); matrizB = Matriz(0, 0); matrizEscalaGrises = Matriz(0, 0)
    histograma = []; rango = (); brillo = 0; contraste = 0; entropia = 0; histogramaAcumulado = []
    
    ruta = str(os.path.dirname(os.path.abspath(__file__)))

    tituloVentana = ""
    if imagen == 1:
        tituloVentana = "Abrir primera imagen"
    else:
        tituloVentana = "Abrir segunda imagen"

    rutaImagen = str(filedialog.askopenfilename(initialdir = ruta,title = tituloVentana))
    imagenAbierta = Image.open(rutaImagen, 'r')

    nombreImagen = rutaImagen[::-1]
    index = 0	
    for i in range(len(nombreImagen)):
        if (nombreImagen[i] == "/"):
            index = i
            break

    nombreImagen = nombreImagen[0:index][::-1]

    columnas, filas = imagenAbierta.size
    tamImg = (columnas, filas)
    
    if imagen == 2 and tamImg != tam:
        return "err"

    # Redimensionar matrices RGB y gris
    matrizR.actualizar(filas, columnas); matrizG.actualizar(filas, columnas); matrizB.actualizar(filas, columnas); matrizEscalaGrises.actualizar(filas, columnas)

    imagenAbierta.show()
    datos = list(imagenAbierta.getdata())

    cont = 0; k = 0
    imarray = numpy.array(imagenAbierta)

    if(len(imarray.shape)<3):
        color = 0
        for i in range(filas):
            if i != filas:
                while (cont < columnas):
                    matrizEscalaGrises.setVal(i, cont, datos[k])
                    cont += 1; k += 1
                cont = 0

    elif len(imarray.shape)==3:
        color = 1
        for i in range(filas):
            if i != filas:
                while (cont < columnas):
                    matrizR.setVal(i, cont, int(datos[k][0]))
                    matrizG.setVal(i, cont, int(datos[k][1]))
                    matrizB.setVal(i, cont, int(datos[k][2]))

                    # Codificación escala de grises PAL
                    matrizEscalaGrises.setVal(i, cont, (round(0.222 * int(datos[k][0]) + round(0.707 * int(datos[k][1]))) + round(0.071 * int(datos[k][2]))))
                    cont += 1; k += 1
                cont = 0

    listaImagenes.append([nombreImagen, filas, columnas, matrizEscalaGrises, matrizR, matrizG, matrizB, histograma, rango, brillo, contraste, entropia, histogramaAcumulado, color])
    indiceIm = len(listaImagenes) - 1

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

    return tamImg, datos


def diferenciaDatos(datos1, datos2):

    datosResult = []

    if (type(datos1[0]) == tuple):
        [datosResult.append([abs(datos1[i][0] - datos2[i][0]), abs(datos1[i][1] - datos2[i][1]), abs(datos1[i][2] - datos2[i][2])]) for i in range(len(datos1))]
 
    else:
        [datosResult.append(abs(datos1[i] - datos2[i])) for i in range(len(datos1))]

    return datosResult


def comprobarUmbral(datos):

    global umbral

    ventana = datos[0]; inputUmbral = datos[1].get()

    if (inputUmbral.isdigit() != True):
        messagebox.showerror("ERROR", f"El umbral debe de ser un número entre 20 y 80")
    else:
        inputUmbral = int(inputUmbral)
        if (inputUmbral < 20 or inputUmbral > 80):
            messagebox.showerror("ERROR", f"El umbral debe de ser un número entre 20 y 80")
        else:
            umbral = inputUmbral
            ventana.destroy()
            calcularMapaCambio()


def calcularMapaCambio():

    global indiceIm; global umbral

    messagebox.showinfo(title="ATENCIÓN", message="A continuación debe añadir dos imagenes del mismo tamaño")
    
    
    imagen1 = abrirImagenesDiferencia(1,0); tamImagen1 = imagen1[0]; datos1 = imagen1[1]
    imagen2 = abrirImagenesDiferencia(2, tamImagen1); datos2 = imagen2[1]

    if imagen2 == "err":
        imagen1("blanco.png")
        fErrorDif()
    else:

        cambio = pintarCambio(datos1,datos2,umbral)

        columnas, filas = tamImagen1
        datos = list(cambio)
        matrizR = Matriz(0, 0); matrizG = Matriz(0, 0); matrizB = Matriz(0, 0); matrizEscalaGrises = Matriz(0, 0)
        matrizR.actualizar(filas, columnas); matrizG.actualizar(filas, columnas); matrizB.actualizar(filas, columnas); matrizEscalaGrises.actualizar(filas, columnas)
        nombreImagen = './backupImagenes/'+listaImagenes[indiceIm][0][:-4]+"MapaCambio.jpg"
        
        cont = 0; k = 0
        color = 1

        for i in range(filas):
            if i != filas:
                while (cont < columnas):
                    matrizR.setVal(i, cont, int(datos[k][0]))
                    matrizG.setVal(i, cont, int(datos[k][1]))
                    matrizB.setVal(i, cont, int(datos[k][2]))

                    # Codificación escala de grises PAL
                    matrizEscalaGrises.setVal(i, cont, (round(0.222 * int(datos[k][0]) + round(0.707 * int(datos[k][1]))) + round(0.071 * int(datos[k][2]))))
                    cont += 1; k += 1
                cont = 0

        listaImagenes.insert(0,[nombreImagen.replace('./backupImagenes/', ""), filas, columnas, matrizEscalaGrises, matrizR, matrizG, matrizB, [], (), 0, 0, 0, [], color])
        indiceIm = len(listaImagenes) - 1

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
        new_image.save(nombreImagen)

        pintarCuadro1(nombreImagen)
        fEtiquetaTam(indiceIm)

        if (len(listaImagenes) == 3):
            fMenuHistorial(0)
        else:
            fMenuHistorial(1)


def pintarCambio(datos1, datos2, umbral):

    if (type(datos1[0]) != tuple):
        datosResult = []
        for i in range(len(datos1)):
            gris1 = datos1[i]
            gris2 = datos2[i]

            resultado = abs(gris1 - gris2)

            if (resultado > umbral):
                datosResult.append((255, 0 ,0))
            else:
                datosResult.append(gris1)
    else:
        datosResult = []
        for i in range(len(datos1)):
            R1 = datos1[i][0]
            G1 = datos1[i][1]
            B1 = datos1[i][2]

            R2 = datos2[i][0]
            G2 = datos2[i][1]
            B2 = datos2[i][2]

            R3 = abs(R1-R2)
            G3 = abs(G1-G2)
            B3 = abs(B1-B2)

            
            if (R3 or G3 or B3) > umbral:
                datosResult.append((255,0, 0))
            else:
                datosResult.append((R1, G1, B1))

    return datosResult