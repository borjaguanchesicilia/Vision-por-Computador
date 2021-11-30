import os
from principal import *


def mostrarTramos(listaDatos):

    if (len(listaPuntos) == listaDatos[1]): # Se han rellenado todos los tramos
        listaDatos[0].destroy()
        if (listaPuntos[len(listaPuntos)-1][1][0] != 255): # No termine en 255, añadir nuevo tramo
            listaPuntos.append(((listaPuntos[len(listaPuntos)-1][1][0], listaPuntos[len(listaPuntos)-1][1][1]), (256, listaPuntos[len(listaPuntos)-1][1][1])))
        else:
            listaPuntos.append(((listaPuntos[len(listaPuntos)-2][1][0], listaPuntos[len(listaPuntos)-2][1][1]), (256, listaPuntos[len(listaPuntos)-1][1][1])))
            listaPuntos.pop(len(listaPuntos)-2)
        if (listaPuntos[0][0][0] != 0): # No empieza en 0, añadir nuevo punto
            listaPuntos.insert(0, ((0, 0), (listaPuntos[0][0][0], listaPuntos[0][0][1])))

        listaX = []; listaY = []

        for i in listaPuntos:
            listaX.append(i[0][0])
            listaY.append(i[0][1])
            listaX.append(i[1][0])
            listaY.append(i[1][1])

        plt.plot(listaX, listaY, '-g')

        for i in range(len(listaPuntos)-1):
            listaX = [listaPuntos[i][0][0], listaPuntos[i][1][0]]
            listaY = [listaPuntos[i][0][1], listaPuntos[i][1][1]]
            plt.plot(listaX, listaY, 'or')

        generarImagenTL()

        plt.show()


def generarImagenTL():

    global nuevosPixels; global valTf

    nuevosPixels = []

    [calcularRecta(listaPuntos[i][0], listaPuntos[i][1]) for i in range(len(listaPuntos))]

    matrizR = Matriz(0, 0); matrizG = Matriz(0, 0); matrizB = Matriz(0, 0); matrizEscalaGrises = Matriz(0, 0)
    matrizR.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizG.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizB.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizEscalaGrises.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])

    j= 0; listaAux = []; pixels = []
    for i in range(listaImagenes[indiceIm][1]):
        if i != listaImagenes[indiceIm][1]:
            while (j< listaImagenes[indiceIm][2]):
                r = nuevosPixels[listaImagenes[indiceIm][4].getVal(i, j)]
                g = nuevosPixels[listaImagenes[indiceIm][5].getVal(i, j)]
                b = nuevosPixels[listaImagenes[indiceIm][6].getVal(i, j)]

                matrizR.setVal(i, j, r)
                matrizG.setVal(i, j, g)
                matrizB.setVal(i, j, b)

                if (listaImagenes[indiceIm][13] == 0):
                    gris = nuevosPixels[listaImagenes[indiceIm][3].getVal(i, j)]
                    matrizEscalaGrises.setVal(i, j, gris)
                    listaAux.append(gris)
                else:
                    # Codificación escala de grises PAL
                    gris = (round(0.222 * r) + round(0.707 * g) + round(0.071 * b))
                    matrizEscalaGrises.setVal(i, j, gris)
                    listaAux.append((r, g, b))

                j+= 1
            pixels.append(listaAux)
            j = 0
            listaAux = []

    array = np.array(pixels, dtype=np.uint8)
    new_image = Image.fromarray(array)

    if valTf != 0:
        nombre = "./backupImagenes/"+listaImagenes[indiceIm][0][:-4]+"TransformacionLineal" + str(valTf) + ".jpg"
        valTf += 1
    else:
        nombre = "./backupImagenes/"+listaImagenes[indiceIm][0][:-4]+"TransformacionLineal.jpg"
        valTf += 1

    new_image.save(nombre)
    pintarCuadro2(nombre)
    listaImagenes.insert(0,[nombre.replace("./backupImagenes/", ""), listaImagenes[indiceIm][1], listaImagenes[indiceIm][2], matrizEscalaGrises, matrizR, matrizG, matrizB, [], (), 0, 0, 0, [], listaImagenes[indiceIm][13]])
    fMenuHistorial()


def calcularRecta(p1, p2):

    global nuevosPixels

    if ((p2[0] - p1[0]) == 0):
        a = 0
    else:
        a = (p2[1] - p1[1]) / (p2[0] - p1[0])
    
    y = 0; it = 0

    inicio = p1[1]; fin = p2[0]-p1[0]
    fin += inicio
 
    for i in range(inicio, fin, 1):
        if a == 0:
            y = p1[1]
        else:
            if it == 0:
                it = 1
                y = p1[1]
            else:
                y += a
        nuevosPixels.append(round(y))


def nuevaVentana(listaDatos):

    global cont; global bIntroducirTramo

    nuevaVentana = Toplevel(listaDatos[0])
    nuevaVentana.title("Transformación Lineal")
    nuevaVentana.geometry("800x800")
    Label(nuevaVentana, text ="Cada tramo viene definido por dos puntos.").grid(row=0, column=0)
    Label(nuevaVentana, text=f"Punto {cont}:  ").grid(row=1, column=0)
    if len(listaPuntos) == 0:
        x = Entry(nuevaVentana)
        x.grid(row=1, column=1)
        y = Entry(nuevaVentana)
        y.grid(row=1, column=2)
    else:
        Label(nuevaVentana, text=f" X = {listaPuntos[cont-1][1][0]}").grid(row=1, column=1)
        Label(nuevaVentana, text=f" Y = {listaPuntos[cont-1][1][1]}").grid(row=1, column=2)
        x = listaPuntos[cont-1][1][0]; y = listaPuntos[cont-1][1][1]
    Label(nuevaVentana, text=f"Punto {cont+1}:  ").grid(row=2, column=0)
    x2 = Entry(nuevaVentana)
    x2.grid(row=2, column=1)
    y2 = Entry(nuevaVentana)
    y2.grid(row=2, column=2)
    
    if (cont == listaDatos[1]-1):
        bIntroducirTramo.destroy()
    if (cont == listaDatos[1]-1):
        Button(nuevaVentana, text='Comprobar punto', command= partial(comprobarPuntos, [x, y, x2, y2, nuevaVentana])).grid(row=6, column=1, sticky=W, pady=4)
        btnMostrar = Button(listaDatos[0], text='Mostrar tramos', command= partial(mostrarTramos, [listaDatos[0], listaDatos[1]]))
        btnMostrar.grid(row=4, column=2)
    else:
        Button(nuevaVentana, text='Comprobar punto', command= partial(comprobarPuntos, [x, y, x2, y2, nuevaVentana])).grid(row=6, column=1, sticky=W, pady=4)

  
def comprobarPuntos(puntos):

    global listaPuntos; global cont

    if (type(puntos[0]) != int):
        p1X = puntos[0].get(); p1Y = puntos[1].get(); p2X = puntos[2].get(); p2Y =puntos[3].get()
    else:
        p1X = str(puntos[0]); p1Y = str(puntos[1]); p2X = puntos[2].get(); p2Y =puntos[3].get()

    if (p1X.isdigit() and p1Y.isdigit() and p2X.isdigit() and p2Y.isdigit()):
        if (len(listaPuntos) != 0):
            if (listaPuntos[cont-1][1][1] >= int(p2Y)):
                messagebox.showerror("ERROR", f"El tramo debe de ser creciente, la coordenada y del punto 1 debe de ser mayor que la del último punto añadido.")
        """if (int(p1Y) >= int(p2Y)):
            messagebox.showerror("ERROR", f"El tramo debe de ser creciente, la coordenada y del punto 2 debe de ser mayor que la del punto 1.")
        else:"""
        listaPuntos.append(((int(p1X), int(p1Y)), (int(p2X), int(p2Y))))
        cont += 1
        puntos[4].destroy()
    else:
        messagebox.showerror("ERROR", "Debe de introducir un número entre 1 y 255")


def comprobarNtramos(listaDatos):

    global listaPuntos; global cont; global bIntroducirTramo; global bComprobarTramos

    listaPuntos = []; cont = 0
    nTramos = listaDatos[1].get()
    num = ["2", "3", "4", "5", "6", "7"]
    if (nTramos.isdigit()):
        if (int(nTramos) > len(num)):
             messagebox.showerror("ERROR", "Debe de introducir un número entre 2 y 7")
        else:
            bComprobarTramos.destroy()
            bIntroducirTramo = Button(listaDatos[0], text ="Introducir nuevo tramo", command= partial(nuevaVentana, [listaDatos[0], int(nTramos)]))
            bIntroducirTramo.grid(row=4, column=2)        
    else:
        messagebox.showerror("ERROR", "Debe de introducir un número entre 2 y 7")          