from operaciones import *


def abrirImagen():
    global borrar; global listaImagenes; global indiceIm
    nombreImagen = ""; filas = 0; columnas = 0
    matrizR = Matriz(0, 0); matrizG = Matriz(0, 0); matrizB = Matriz(0, 0); matrizEscalaGrises = Matriz(0, 0)
    histograma = []; rango = (); brillo = 0; contraste = 0; entropia = 0; histogramaAcumulado = []
    
    ruta = str(os.path.dirname(os.path.abspath(__file__)))
    rutaImagen = str(filedialog.askopenfilename(initialdir = ruta,title = "Abrir imagen",filetypes = (("Imagenes","*.jpg;*.png"),("All files","*.*"))))
    imagen = Image.open(rutaImagen, 'r')
    #imagen.show()
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

    # Mostrar imagen + imagen blanco
    imagen1(nombreImagen); imagen2("blanco.png")

    cont = 0; k = 0

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

    listaImagenes.insert(0, [nombreImagen, filas, columnas, matrizEscalaGrises, matrizR, matrizG, matrizB, histograma, rango, brillo, contraste, entropia, histogramaAcumulado])
    indiceIm = 0
    fEtiquetaTam()

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
    
    # Menu de historial de imagenes
    fMenuHistorial(borrar)
    borrar = 1
    

def guardar():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))


def guardarComo():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))


def fError():
   messagebox.showerror("ERROR", "Debe de abrir una imagen")


def fHistograma():  # Indice 7

    if (len(listaImagenes) != 0):
        if(len(listaImagenes[indiceIm][7]) == 0): # No se ha calculado el histograma
            listaImagenes[indiceIm][7] = calcularHistograma(listaImagenes[indiceIm][3], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
        graficarHistograma(listaImagenes[indiceIm][7], "Histograma de la imagen "+listaImagenes[indiceIm][0])
    else:
        fError()


def fHistogramaAcumulado():  # Indice 12

    if (len(listaImagenes) != 0):
        if(len(listaImagenes[indiceIm][7]) == 0): # No se ha calculado el histograma
            listaImagenes[indiceIm][7] = calcularHistograma(listaImagenes[indiceIm][3], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
        if(len(listaImagenes[indiceIm][12]) == 0): # No se ha calculado el histograma acumulado
            listaImagenes[indiceIm][12] = calcularHistogramaAcumulado(listaImagenes[indiceIm][7])
        graficarHistograma(listaImagenes[indiceIm][12], "Histograma acumulado de la imagen "+listaImagenes[indiceIm][0])
    else:
        fError()


def fRango(): # Indice 8

    if (len(listaImagenes) != 0):
        if (len(listaImagenes[indiceIm][8]) == 0):
            if (len(listaImagenes[indiceIm][7]) == 0):
                listaImagenes[indiceIm][7] = calcularHistograma(listaImagenes[indiceIm][3], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
            listaImagenes[indiceIm][8] = calcularRango(listaImagenes[indiceIm][7])
        messagebox.showinfo(title="Rango de valores", message=f"El rango de valores es: [{str(listaImagenes[indiceIm][8][0])}, {str(listaImagenes[indiceIm][8][1])}]")
    else:
        fError()


def fBrillo():  # Indice 9

    if (len(listaImagenes) != 0):
        if (listaImagenes[indiceIm][9] == 0):
            if (len(listaImagenes[indiceIm][7]) == 0):
                listaImagenes[indiceIm][7] = calcularHistograma(listaImagenes[indiceIm][3], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
            listaImagenes[indiceIm][9] = calcularBrillo(listaImagenes[indiceIm][7], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
        messagebox.showinfo(title="Brillo", message=f"El brillo es: {str(listaImagenes[indiceIm][9])}")
    else:
        fError()


def fContraste():  # Indice 10

    if (len(listaImagenes) != 0):
        if (listaImagenes[indiceIm][10] == 0):
            if (listaImagenes[indiceIm][9] == 0):
                if (len(listaImagenes[indiceIm][7]) == 0):
                    listaImagenes[indiceIm][7] = calcularHistograma(listaImagenes[indiceIm][3], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
                listaImagenes[indiceIm][9] = calcularBrillo(listaImagenes[indiceIm][7], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
            listaImagenes[indiceIm][10] = calcularContraste(listaImagenes[indiceIm][7], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2], listaImagenes[indiceIm][9])
        messagebox.showinfo(title="Contraste", message=f"El contraste es: {str(listaImagenes[indiceIm][10])}")
    else:
        fError()


def fEntropia():  # Indice 11

    if (len(listaImagenes) != 0):
        if (listaImagenes[indiceIm][11] == 0):
            if (len(listaImagenes[indiceIm][7]) == 0):
                listaImagenes[indiceIm][7] = calcularHistograma(listaImagenes[indiceIm][3], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
            listaImagenes[indiceIm][11] = calcularEntropia(listaImagenes[indiceIm][7], listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])
        messagebox.showinfo(title="Entropía", message=f"La entropía es: {str(listaImagenes[indiceIm][11])}")
    else:
        fError()


def fRoi():

    if (len(listaImagenes) != 0):
        calcularRoi()
    else:
        fError()


def fNegativo():

    if (len(listaImagenes) != 0):
        nombre = calcularNegativo()
        imagen2(nombre)
    else:
        fError()


def fTransformacionLineal():

    if (len(listaImagenes) != 0):
        transformacionLineal()
    else:
        fError()


def fCorreccionGamma():

    if (len(listaImagenes) != 0):
        calcularCorreccionGamma()
    else:
        fError()


def fDiferencia():

    print(
        "gfgfgf"
    )
