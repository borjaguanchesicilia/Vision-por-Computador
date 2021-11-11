from math import gamma
from typing import Tuple
from principal import *


def comprobarDatosGamma(listaDatos):

    global valorGamma

    gamma = listaDatos[0].get()

    try:
        gamma = float(gamma)
        if (0.05 <= gamma and gamma <= 20):
            valorGamma = gamma
            listaDatos[1].destroy()
            correccionGamma()
        else:
            messagebox.showerror("ERROR", "Debe de introducir un número (0.05 <= gammma >= 20)")


    except ValueError:
        messagebox.showerror("ERROR", "Debe de introducir un número (0.05 <= gammma >= 20)")
    
        
def correccionGamma():

    global valorGamma;

    matrizR = Matriz(0, 0); matrizG = Matriz(0, 0); matrizB = Matriz(0, 0); matrizEscalaGrises = Matriz(0, 0)
    matrizR.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizG.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizB.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizEscalaGrises.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])

    j = 0; listaAux = []; pixels = []

    for i in range(listaImagenes[indiceIm][1]):
        if i != listaImagenes[indiceIm][1]:
            while (j < listaImagenes[indiceIm][2]):
                aR = listaImagenes[indiceIm][4].getVal(i, j) / 255
                bR = pow(aR, valorGamma)
                r = round(bR * 255)

                aG = listaImagenes[indiceIm][5].getVal(i, j) / 255
                bG = pow(aG, valorGamma)
                g = round(bG * 255)

                aB = listaImagenes[indiceIm][6].getVal(i, j) / 255
                bB = pow(aB, valorGamma)
                b =  round(bB * 255)
                
                
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
    nombre = "./backupImagenes/"+listaImagenes[indiceIm][0][:-4]+"CorreccionGamma.jpg"
    new_image.save(nombre)
    imagen2(nombre)

    listaImagenes.append([str(listaImagenes[indiceIm][0][:-4]+"CorreccionGamma.jpg"), listaImagenes[indiceIm][1], listaImagenes[indiceIm][2], matrizEscalaGrises, matrizR, matrizG, matrizB, [], (), 0, 0, 0, []])
    fMenuHistorial()