import numpy
from principal import *
from operaciones import *


def previsualizarAjusteLineal(datos):

    global brilloAl; global contrasteAl; global valAl

    brilloAl = int(datos[0].get()); contrasteAl = int(datos[1].get())


    if (listaImagenes[indiceIm][9] == 0):
        if (len(listaImagenes[indiceIm][7]) == 0):
            listaImagenes[indiceIm][7] = calcularHistograma(listaImagenes[indiceIm][3], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
        listaImagenes[indiceIm][9] = calcularBrillo(listaImagenes[indiceIm][7], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
    
    if (listaImagenes[indiceIm][10] == 0):
            listaImagenes[indiceIm][10] = calcularContraste(listaImagenes[indiceIm][7], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2], listaImagenes[indiceIm][9])

    if (listaImagenes[indiceIm][10] == 0 or contrasteAl == 0):
        valA = 0
    else:
        valA = contrasteAl / listaImagenes[indiceIm][10]

    valB = brilloAl - valA * listaImagenes[indiceIm][9]

    matrizR = Matriz(0, 0); matrizG = Matriz(0, 0); matrizB = Matriz(0, 0); matrizEscalaGrises = Matriz(0, 0)
    matrizR.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizG.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizB.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizEscalaGrises.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])

    cont = 0; listaAux = []; pixels = []

    for i in range(listaImagenes[indiceIm][1]):
        if i != listaImagenes[indiceIm][1]:
            while (cont < listaImagenes[indiceIm][2]):
                r = round(valA * listaImagenes[indiceIm][4].getVal(i, cont) + valB)
                g = round(valA * listaImagenes[indiceIm][5].getVal(i, cont) + valB)
                b = round(valA * listaImagenes[indiceIm][6].getVal(i, cont) + valB)
                if (r < 0): r = 0
                elif (r > 255): r = 255 
                if (g < 0): g = 0
                elif (g > 255): g = 255 
                if (b < 0): b = 0
                elif (b > 255): b = 255 

                matrizR.setVal(i, cont, r)
                matrizG.setVal(i, cont, g)
                matrizB.setVal(i, cont, b)

                if (listaImagenes[indiceIm][13] == 0):
                    gris = valA * listaImagenes[indiceIm][3].getVal(i, cont) + valB
                    if (gris < 0): gris = 0
                    elif (gris > 255): gris = 255
                    matrizEscalaGrises.setVal(i, cont, gris)
                    listaAux.append(gris)
                else:
                    # Codificación escala de grises PAL
                    gris = (round(0.222 * r) + round(0.707 * g) + round(0.071 * b))
                    matrizEscalaGrises.setVal(i, cont, gris)
                    listaAux.append((r, g, b))

                cont += 1
            pixels.append(listaAux)
            cont = 0
            listaAux = []

    array = np.array(pixels, dtype=np.uint8)
    new_image = Image.fromarray(array)

    if valAl != 0:
        nombre = "./backupImagenes/"+listaImagenes[indiceIm][0][:-4]+"AjusteLineal" + str(valAl) + ".jpg"
        valAl += 1
    else:
        nombre = "./backupImagenes/"+listaImagenes[indiceIm][0][:-4]+"AjusteLineal.jpg"
        valAl += 1


    new_image.save(nombre)
    pintarCuadro2(nombre)
    listaImagenes.insert(0,[nombre.replace("./backupImagenes/", ""), listaImagenes[indiceIm][1], listaImagenes[indiceIm][2], matrizEscalaGrises, matrizR, matrizG, matrizB, [], (), brilloAl, contrasteAl, 0, [], listaImagenes[indiceIm][13]])



def aplicarAjusteLineal(ventana):

    fMenuHistorial()

    ventana.destroy()