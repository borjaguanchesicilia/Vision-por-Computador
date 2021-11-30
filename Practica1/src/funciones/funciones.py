import numpy
from operaciones import *
from funciones import funcionesDf as diferencia


def abrirImagen():

    global listaImagenes; global indiceIm
    nombreImagen = ""; filas = 0; columnas = 0
    matrizR = Matriz(0, 0); matrizG = Matriz(0, 0); matrizB = Matriz(0, 0); matrizEscalaGrises = Matriz(0, 0)
    histograma = []; rango = (); brillo = 0; contraste = 0; entropia = 0; histogramaAcumulado = []
        
    ruta = str(os.path.dirname(os.path.abspath(__file__)))
    rutaImagen = str(filedialog.askopenfilename(initialdir = ruta,title = "Abrir imagen"))
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

    # Mostrar imagen + imagen blanco
    pintarCuadro1(rutaImagen); pintarCuadro2("./funciones/blanco.png")

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

    listaImagenes.insert(0, [nombreImagen, filas, columnas, matrizEscalaGrises, matrizR, matrizG, matrizB, histograma, rango, brillo, contraste, entropia, histogramaAcumulado, color])
    
    fEtiquetaTam(indiceIm)

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
    
    if (len(listaImagenes) == 1):
        fMenuHistorial(0)
    else:
        fMenuHistorial()
    

def guardarComo():

    ruta = filedialog.asksaveasfilename(initialdir = "/",title = "Guardar como")

    nombreImagen = listaImagenes[indiceIm][0]
    imagen = Image.open('./backupImagenes/'+nombreImagen)

    columnas, filas = imagen.size
    datos = list(imagen.getdata())

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
    new_image.save(ruta)


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
        pintarCuadro2(nombre)
    else:
        fError()


def fAjusteLineal():

    if (len(listaImagenes) != 0):
        calcularAjusteLineal()
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


def fEspecificacionHistograma():

    if (len(listaImagenes) != 0):
        calcularEspecificacion()
    else:
        fError()


def fEcualizacionHistograma():

    if (len(listaImagenes) != 0):
        calcularEcualizacion()
    else:
        fError()


def fInfoPixel():

    if (len(listaImagenes) != 0):
        infoPixel()
    else:
        fError()


def fDiferencia():

    global indiceIm

    messagebox.showinfo(title="ATENCIÓN", message="A continuación debe añadir dos imagenes del mismo tamaño")
    imagen1 = diferencia.abrirImagenesDiferencia(1,0); tamImagen1 = imagen1[0]; datos1 = imagen1[1]
    imagen2 = diferencia.abrirImagenesDiferencia(2, tamImagen1); datos2 = imagen2[1]

    if imagen2 == "err":
        pintarCuadro1("./funciones/blanco.png")
        diferencia.fErrorDif()
    else:

        dif = diferencia.diferenciaDatos(datos1,datos2)
        imarray = numpy.array(dif)
        columnas, filas = tamImagen1
        datos = list(dif)
        matrizR = Matriz(0, 0); matrizG = Matriz(0, 0); matrizB = Matriz(0, 0); matrizEscalaGrises = Matriz(0, 0)
        matrizR.actualizar(filas, columnas); matrizG.actualizar(filas, columnas); matrizB.actualizar(filas, columnas); matrizEscalaGrises.actualizar(filas, columnas)
        nombreImagen = "./backupImagenes/"+listaImagenes[len(listaImagenes)-1][0][:-4]+"Diferencia.jpg"
        
        cont = 0; k = 0

        if(len(imarray.shape)<3):
            color = 0
            for i in range(filas):
                if i != filas:
                    while (cont < columnas):
                        matrizEscalaGrises.setVal(i, cont, datos[k][0])
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

        listaImagenes.insert(0,[nombreImagen.replace("./backupImagenes/", ""), filas, columnas, matrizEscalaGrises, matrizR, matrizG, matrizB, [], (), 0, 0, 0, [], color])

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
            fMenuHistorial()


def fMapaCambio():

    ventanaMapa = Toplevel(app)
    ventanaMapa.title("Mapa de cambio")
    ventanaMapa.geometry("300x300")

    etiquetaTexto = Label(ventanaMapa, text ="Introduzca el umbral"); etiquetaTexto.grid(row=0, column=0)
    inputUmbral = Entry(ventanaMapa); inputUmbral.grid(row=0, column=1)

    bComprobar = Button(ventanaMapa, text ="Click para comprobar", command= partial(diferencia.comprobarUmbral, [ventanaMapa, inputUmbral]))
    bComprobar.grid(row=2, column=0)


def fPerfil():

    if (len(listaImagenes) != 0):
        calcularPerfil()
    else:
        fError()