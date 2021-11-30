from matplotlib.pyplot import legend
from principal import *
from tkinter import messagebox
import copy
 

def comprobarRecta(datos):

    ventana = datos[0]; punto1X = datos[1][0][0].get(); punto1Y = datos[1][0][1].get(); punto2X = datos[1][1][0].get(); punto2Y = datos[1][1][1].get()

    if (punto1X.isdigit() != True or punto1Y.isdigit() != True or punto2X.isdigit() != True or punto2Y.isdigit() != True):
        messagebox.showerror("ERROR", f"Debe introduzca dos puntos, con 1 <= X >= {listaImagenes[indiceIm][1]} e 0 <= Y >= {listaImagenes[indiceIm][2]}")
    else:
        punto1X = int(punto1X); punto1Y = int(punto1Y); punto2X = int(punto2X); punto2Y = int(punto2Y)
        if ((1 > punto1X) or (punto1X > listaImagenes[indiceIm][1])):
            messagebox.showerror("ERROR", f"El punto 1 X debe ser:  1 <= X >= {listaImagenes[indiceIm][1]}")
        elif ((1 > punto2X) or (punto2X > listaImagenes[indiceIm][1])):
            messagebox.showerror("ERROR", f"El punto 2 X debe ser:  1 <= X >= {listaImagenes[indiceIm][1]}")
        elif ((1 > punto1Y) or (punto1Y > listaImagenes[indiceIm][2])):
            messagebox.showerror("ERROR", f"El punto 1 Y debe ser:  1 <= Y >= {listaImagenes[indiceIm][2]}")
        elif ((1 > punto2Y) or (punto2Y > listaImagenes[indiceIm][2])):
            messagebox.showerror("ERROR", f"El punto 2 Y debe ser:  1 <= Y >= {listaImagenes[indiceIm][2]}")
        else:
            ventana.destroy()
            imagen = Image.open("./backupImagenes/"+listaImagenes[indiceIm][0], 'r')
            imagenP = ImageDraw.Draw(imagen)
            imagenP.line((punto1X,punto1Y, punto2X,punto2Y), fill=255, width=6)
            imagen.show()

            a = (punto2Y - punto1Y) / (punto2X - punto1X)
            b = punto1Y / (a * punto1X)

            if (punto1Y > punto2Y):
                punto1Y, punto2Y = punto2Y, punto1Y

            if (punto1X > punto2X):
                punto1X, punto2X = punto2X, punto1X

            if ((punto2Y - punto1Y) > (punto2X - punto1X)):

                # Le damos valores a la Y:
                valoresY = [] # Lista de valores de y
                valoresX = [] # Lista de valores de x dando valores a y
                valoresY = []
                valorY = punto1Y
                while(valorY < punto2Y-1):
                    x = abs(int(valorY / a - b))
                    valoresY.append(valorY)
                    valoresX.append(x)
                    valorY += 1
                
                valoresX.pop(); valoresY.pop()
                perfil = []; perfilD = []; perfilSuavizado = []; perfilSuavizadoD = []
                [perfil.append(listaImagenes[indiceIm][3].getVal(valoresX[i], valoresY[i])) for i in range(len(valoresX))]
                [perfilD.append(perfil[i] - (perfil[i+1] - perfil[i])) for i in range(len(valoresX)) if (i != len(valoresX) - 1)]

                media = perfil[0]
                for i in range(1, len(perfil)-1, 1):
                    media = int((media + perfil[i] + perfil[i+1]) / 3)
                    perfilSuavizado.append(media) 

                media = perfilD[0]
                for i in range(1, len(perfilD)-1, 1):
                    media = int((media + perfilD[i] + perfilD[i+1]) / 3)
                    perfilSuavizadoD.append(media) 

                graficarPerfil(valoresY, perfil, perfilSuavizado, listaImagenes[indiceIm][0])
                graficarPerfil(valoresY, perfilD, perfilSuavizadoD, listaImagenes[indiceIm][0], "derivado")

            else:

                # Le damos valores a la X:
                valoresY = [] # Lista de valores de y dando valores a x
                valoresX = [] # Lista de valores de X
                valorX = punto1X
                while(valorX < punto2X-1):
                    y = abs(int(a * valorX + b))
                    valoresX.append(valorX)
                    valoresY.append(y)
                    valorX += 1

                perfil = []; perfilD = []; perfilSuavizado = []; perfilSuavizadoD = []
                [perfil.append(listaImagenes[indiceIm][3].getVal(valoresX[i], valoresY[i])) for i in range(len(valoresX))]
                [perfilD.append(perfil[i] - (perfil[i+1] - perfil[i])) for i in range(len(valoresX)) if (i != len(valoresX) - 1)]

                media = perfil[0]
                for i in range(1, len(perfil)-1, 1):
                    media = int((media + perfil[i] + perfil[i+1]) / 3)
                    perfilSuavizado.append(media) 

                media = perfilD[0]
                for i in range(1, len(perfilD)-1, 1):
                    media = int((media + perfilD[i] + perfilD[i+1]) / 3)
                    perfilSuavizadoD.append(media) 

                graficarPerfil(valoresX, perfil, perfilSuavizado, listaImagenes[indiceIm][0])
                graficarPerfil(valoresX, perfilD, perfilSuavizadoD, listaImagenes[indiceIm][0], "derivado")


def graficarPerfil(valoresX, perfil, perfilS, nombre, der=""):

    if der == "":
        valoresXCambio = copy.deepcopy(valoresX)

        valoresXSuavizado = copy.deepcopy(valoresXCambio)
        valoresXSuavizado.pop(0)
        valoresXSuavizado.pop()

    else:
        valoresXCambio = copy.deepcopy(valoresX); valoresXCambio.pop()

        valoresXSuavizado = copy.deepcopy(valoresXCambio)
        valoresXSuavizado.pop(0)
        valoresXSuavizado.pop()

    plt.figure("Perfil " + nombre + der)
    plt.title("Perfil " + nombre + der)
    plt.xlabel("Puntos")
    plt.ylabel("Niveles de gris")
    plt.plot(valoresXCambio, perfil, "-r", linewidth=4.0, label=f'Perfil {der}')
    plt.plot(valoresXSuavizado, perfilS, "-b", linewidth=2.0, label=f'Perfil {der} Suavizado')
    plt.legend(loc="upper left")
    plt.show()