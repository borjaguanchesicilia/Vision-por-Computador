import numpy
from principal import *


def previsualizarAjusteLineal(datos):

    brillo = datos[0].get(); contraste = datos[1].get()

    if (contraste == listaImagenes[indiceIm][10]):
        valA = 1
    else:
        valA = contraste / listaImagenes[indiceIm][10]

    if (brillo == listaImagenes[indiceIm][9]):
        valB = 0
    else:
        valB = brillo - valA * listaImagenes[indiceIm][9]

    matrizR = Matriz(0, 0); matrizG = Matriz(0, 0); matrizB = Matriz(0, 0); matrizEscalaGrises = Matriz(0, 0)
    matrizR.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizG.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizB.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizEscalaGrises.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])

    cont = 0; listaAux = []; pixels = []

    for i in range(listaImagenes[indiceIm][1]):
        if i != listaImagenes[indiceIm][1]:
            while (cont < listaImagenes[indiceIm][2]):
                r = valA * listaImagenes[indiceIm][4].getVal(i, cont) + valB
                g = valA * listaImagenes[indiceIm][5].getVal(i, cont) + valB
                b = valA * listaImagenes[indiceIm][6].getVal(i, cont) + valB
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
    nombre = "./backupImagenes/"+listaImagenes[indiceIm][0][:-4]+"AjusteLineal.jpg"
    new_image.save(nombre)

    pintarCuadro2(nombre)


def aplicarAjusteLineal(ventana):

    rutaImagen = "./backupImagenes/"+listaImagenes[indiceIm][0][:-4]+"AjusteLineal.jpg"

    matrizR = Matriz(0, 0); matrizG = Matriz(0, 0); matrizB = Matriz(0, 0); matrizEscalaGrises = Matriz(0, 0)
    histograma = []; rango = (); brillo = 0; contraste = 0; entropia = 0; histogramaAcumulado = []

    imagen = Image.open(rutaImagen, 'r')

    nombreImagen = rutaImagen[::-1]
    index = 0	
    for i in range(len(nombreImagen)):
        if (nombreImagen[i] == "/"):
            index = i
            break

    nombreImagen = nombreImagen[0:index][::-1]

    columnas, filas = imagen.size
    datos = list(imagen.getdata())

    # Redimensionar matrices RGB y gris
    matrizR.actualizar(filas, columnas); matrizG.actualizar(filas, columnas); matrizB.actualizar(filas, columnas); matrizEscalaGrises.actualizar(filas, columnas)

    # Mostrar imagen
    pintarCuadro2(rutaImagen)

    imarray = numpy.array(imagen)
    cont = 0; k = 0

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

    listaImagenes.insert(0,[nombreImagen, filas, columnas, matrizEscalaGrises, matrizR, matrizG, matrizB, histograma, rango, brillo, contraste, entropia, histogramaAcumulado, color])

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
    
    fMenuHistorial()

    ventana.destroy()