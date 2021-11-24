from os import remove
from PIL import ImageDraw
from principal import *


def comprobarPuntos(listaDatos):

    filas = listaImagenes[indiceIm][1]; columnas = listaImagenes[indiceIm][2]

    listaPuntos = listaDatos[1]
    puntos = []

    # Se comprueba si todos los puntos son numero enteros:
    for i in range(len(listaPuntos)):
        if ((listaPuntos[i][0].get().isdigit() == False) or (listaPuntos[i][1].get().isdigit() == False)):
                messagebox.showerror("ERROR", f"Debe de introducir un número entero: (0 <= X >= {columnas},  0 <= Y >= {filas})")
                break
        else:
            if ((int(listaPuntos[i][0].get()) > columnas) or (int(listaPuntos[i][1].get()) > filas)):
                messagebox.showerror("ERROR", f"Debe de introducir un punto: (0 <= X >= {columnas},  0 <= Y >= {filas})")
                break
            else:
                puntos.append((int(listaPuntos[i][0].get()), int(listaPuntos[i][1].get())))

    if(len(puntos) == 4):
        if (puntos[0][0] != puntos[2][0]):
            messagebox.showerror("ERROR", "Las coordenadas x de los puntos 1 y 3 tienen que ser iguales")
        else:
            if (puntos[1][0] != puntos[3][0]):
                messagebox.showerror("ERROR", "Las coordenadas x de los puntos 2 y 4 tienen que ser iguales")
            else:
                if (puntos[0][1] != puntos[1][1]):
                    messagebox.showerror("ERROR", "Las coordenadas y de los puntos 1 y 2 tienen que ser iguales")
                else:
                    if (puntos[2][1] != puntos[3][1]):
                        messagebox.showerror("ERROR", "Las coordenadas y de los puntos 3 y 4 tienen que ser iguales")
                    else:

                        fCopiaImagen(listaImagenes[indiceIm][0])
                        nombre = "./backupImagenes/" + listaImagenes[indiceIm][0][:-4] + "Copia.jpg"
                        im = Image.open(nombre)
                        draw = ImageDraw.Draw(im)
                        draw.line((puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1]), fill ="red", width = 2)
                        draw.line((puntos[2][0], puntos[2][1], puntos[3][0], puntos[3][1]), fill ="red", width = 2)
                        draw.line((puntos[0][0], puntos[0][1], puntos[2][0], puntos[2][1]), fill ="red", width = 2)
                        draw.line((puntos[1][0], puntos[1][1], puntos[3][0], puntos[3][1]), fill ="red", width = 2)
                        
                        array = np.array(im, dtype=np.uint8)
                        new_image = Image.fromarray(array)
                        new_image.save(nombre.replace("Copia", "ROIrojo"))
                        pintarCuadro2(nombre.replace("Copia", "ROIrojo"))
                        remove(nombre)

                        bAceptarRoi = Button(listaDatos[0], text ="Click para aceptar ROI", command= partial(confirmarRoi, [listaDatos[0], puntos]))
                        bAceptarRoi.grid(row=7, column=0)


def confirmarRoi(datos):

    datos[0].destroy()

    filas = datos[1][3][1]-datos[1][0][1]; columnas = datos[1][3][0]-datos[1][0][0]

    matrizR = Matriz(0, 0); matrizG = Matriz(0, 0); matrizB = Matriz(0, 0); matrizEscalaGrises = Matriz(0, 0)
    matrizR.actualizar(filas, columnas); matrizG.actualizar(filas, columnas); matrizB.actualizar(filas, columnas); matrizEscalaGrises.actualizar(filas, columnas)

    j = datos[1][0][0]; listaAux = []; pixels = []

    for i in range(datos[1][0][1], datos[1][3][1], 1):
        if i != datos[1][3][1]:
            while (j < datos[1][3][0]-1):
                r = listaImagenes[indiceIm][4].getVal(i, j)
                g = listaImagenes[indiceIm][5].getVal(i, j)
                b = listaImagenes[indiceIm][6].getVal(i, j)

                matrizR.setVal(i-datos[1][0][1], j-datos[1][0][0], r)
                matrizG.setVal(i-datos[1][0][1], j-datos[1][0][0], g)
                matrizB.setVal(i-datos[1][0][1], j-datos[1][0][0], b)

                if (listaImagenes[indiceIm][13] == 0):
                    gris = listaImagenes[indiceIm][3].getVal(i, j)
                    matrizEscalaGrises.setVal(i, j, gris)
                    listaAux.append(gris)
                else:
                    # Codificación escala de grises PAL
                    gris = (round(0.222 * r) + round(0.707 * g) + round(0.071 * b))
                    matrizEscalaGrises.setVal(i-datos[1][0][1], j-datos[1][0][0], gris)
                    listaAux.append((r, g, b))
                j += 1

            pixels.append(listaAux)
            j = datos[1][0][0]
            listaAux = []

    array = np.array(pixels, dtype=np.uint8)
    new_image = Image.fromarray(array)
    nombre = "./backupImagenes/"+listaImagenes[indiceIm][0][:-4]+"Roi.jpg"
    new_image.save(nombre)

    listaImagenes.insert(0,[str(listaImagenes[indiceIm][0][:-4]+"Roi.jpg"), filas, columnas, matrizEscalaGrises, matrizR, matrizG, matrizB, [], (), 0, 0, 0, [], listaImagenes[indiceIm][13]])
                        
    fMenuHistorial()


def comprobarPixel(listaDatos):

    pixelX = listaDatos[0][0].get(); pixelY = listaDatos[0][1].get()

    if ((pixelX.isdigit() == False) or (pixelY.isdigit() == False)):
        messagebox.showerror("ERROR", f"Debe de introducir un número entero: (0 <= X >= {listaImagenes[indiceIm][1]},  0 <= Y >= {listaImagenes[indiceIm][2]})")
    else:
        if(int(pixelX) < 0 or int(pixelY) < 0):
            messagebox.showerror("ERROR", "Debe de introducir un pixel con coordenadas <= 0")
        else: 
            if(int(pixelX) > listaImagenes[indiceIm][1]):
                messagebox.showerror("ERROR", f"Debe de introducir una coordena X para el pixel: (X <= {listaImagenes[indiceIm][1]}")
            else:          
                if(int(pixelY) > listaImagenes[indiceIm][2]):
                    messagebox.showerror("ERROR", f"Debe de introducir una coordena Y para el pixel: (Y <= {listaImagenes[indiceIm][2]}")
                else:
                    etiquetaInfoPixel = Label(listaDatos[1], text =f"(R: {listaImagenes[indiceIm][4].getVal(int(pixelX), int(pixelY))} G: {listaImagenes[indiceIm][5].getVal(int(pixelX), int(pixelY))} B: {listaImagenes[indiceIm][6].getVal(int(pixelX), int(pixelY))})")
                    etiquetaInfoPixel.grid(row=2, column=0)