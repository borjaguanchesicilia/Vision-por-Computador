from principal import *


def mostrarTramos(listaDatos):
    if (len(listaPuntos) == listaDatos[1]): # Se han rellenado todos los tramos
        listaDatos[0].destroy()
        if (listaPuntos[len(listaPuntos)-1][0] != 255): # No termine en 255, añadir nuevo tramo
            listaPuntos.append((255, listaPuntos[len(listaPuntos)-1][1]))

        if (listaPuntos[0][1] != 0): # No termine en 255, añadir nuevo tramo
            listaPuntos.insert(0, (0, 0))

        listaX = []; listaY = []


        for i in range(len(listaPuntos)):
            listaX.append(listaPuntos[i][0])
            listaY.append(listaPuntos[i][1])

        plt.plot(listaX, listaY, '-g')

        for i in range(len(listaPuntos)-1):
            listaX = [listaPuntos[i][0], listaPuntos[i+1][0]]
            listaY = [listaPuntos[i][1], listaPuntos[i+1][1]]
            plt.plot(listaX, listaY, 'or')

        generarImagenTL()

        plt.show()


def generarImagenTL():

    for i in range(len(listaPuntos)-1):
        p1 = listaPuntos[i]; p2 = listaPuntos[i+1]
        calcularRecta(p1, p2)

    matrizR = Matriz(0, 0); matrizG = Matriz(0, 0); matrizB = Matriz(0, 0); matrizEscalaGrises = Matriz(0, 0)
    matrizR.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizG.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizB.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2]); matrizEscalaGrises.actualizar(listaImagenes[indiceIm][1], listaImagenes[indiceIm][2])

    cont = 0; listaAux = []; pixels = []
    for i in range(listaImagenes[indiceIm][1]):
        if i != listaImagenes[indiceIm][1]:
            while (cont < listaImagenes[indiceIm][2]):
                r = nuevosPixels[listaImagenes[indiceIm][4].getVal(i, cont)]
                g = nuevosPixels[listaImagenes[indiceIm][5].getVal(i, cont)]
                b = nuevosPixels[listaImagenes[indiceIm][6].getVal(i, cont)]

                matrizR.setVal(i, cont, r)
                matrizG.setVal(i, cont, g)
                matrizB.setVal(i, cont, b)

                if (listaImagenes[indiceIm][13] == 0):
                    gris = nuevosPixels[listaImagenes[indiceIm][3].getVal(i, cont)]
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
    nombre = "./backupImagenes/"+listaImagenes[indiceIm][0][:-4]+"TransformacionLineal.jpg"
    new_image.save(nombre)
    pintarCuadro2(nombre)
    listaImagenes.insert(0,[str(listaImagenes[indiceIm][0][:-4]+"TransformacionLineal.jpg"), listaImagenes[indiceIm][1], listaImagenes[indiceIm][2], matrizEscalaGrises, matrizR, matrizG, matrizB, [], (), 0, 0, 0, [], listaImagenes[indiceIm][13]])
    fMenuHistorial()


def calcularRecta(p1, p2):

    global nuevosPixels

    multX = 1; multY = 1;
    multX = round(multX * (p2[1] - p1[1])); multY = round(multY * (p2[0] - p1[0]))
    parte1 = round(p1[0] * (-1) * (p2[1] - p1[1]))
    parte2 = round(p1[1] * (-1) * (p2[0] - p1[0]))
    for i in range(p1[0], p2[0]+1, 1):
        y = round((multX * i + parte1 + parte2 * (-1)) / multY)
        nuevosPixels.append(y)


def nuevaVentana(listaDatos):

    global cont; global bIntroducirTramo

    nuevaVentana = Toplevel(listaDatos[0])
    nuevaVentana.title("Transformación Lineal")
    nuevaVentana.geometry("500x500")
    Label(nuevaVentana, text ="Introduzca los tramos para la transformación lineal. Debe introducir puntos.")
    Label(nuevaVentana, text=f"Punto {cont}:  ").grid(row=0)
    if(len(listaPuntos) == 0):
        Label(nuevaVentana, text=" x > 0").grid(row=0, column=3)
    else:
        Label(nuevaVentana, text=f" x > {listaPuntos[cont-2][0]}").grid(row=0, column=3)
        Label(nuevaVentana, text=f"  y > {listaPuntos[cont-2][1]}").grid(row=0, column=4)
    x = Entry(nuevaVentana)
    x.grid(row=0, column=1)
    y = Entry(nuevaVentana)
    y.grid(row=0, column=2)
    print(cont, listaDatos[1])

    if (cont == listaDatos[1]):
        bIntroducirTramo.destroy()
    if (cont == listaDatos[1]):
        Button(nuevaVentana, text='Comprobar punto', command= partial(comprobarPunto, [x, y, nuevaVentana])).grid(row=3, column=1, sticky=W, pady=4)
        btnMostrar = Button(listaDatos[0], text='Mostrar tramos', command= partial(mostrarTramos, [listaDatos[0], listaDatos[1]]))
        btnMostrar.grid(row=3, column=2)
    else:
        Button(nuevaVentana, text='Comprobar punto', command= partial(comprobarPunto, [x, y, nuevaVentana])).grid(row=3, column=1, sticky=W, pady=4)



    
    
        
    
def comprobarPunto(puntos):

    global listaPuntos; global cont
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '249', '250', '251', '252', '253', '254', '255']
    if (str(puntos[1].get()).isdigit() and str(puntos[0].get()).isdigit()):
        if(len(listaPuntos) == 0): # Si se va a introducir el primer punto
            if (int(puntos[0].get()) <= 0): # Si se va a introducir el primer punto y la x = 0
                messagebox.showerror("ERROR", "Debe de introducir un número mayor que 0")
        else: # Si se va a introducir un punto != primer punto
            if (int(puntos[0].get()) <= listaPuntos[cont-2][0]): # Se comprueba que la x sea mayor que la x del punto anterior
                messagebox.showerror("ERROR", f"Debe de introducir un número mayor que {listaPuntos[cont-2][0]}")
        
        if ((int(puntos[1].get()) != int(num[int(puntos[1].get())])) or (int(puntos[0].get()) != int(num[int(puntos[0].get())]))): # Comprobar si la x e y son números entre 0 y 255
            messagebox.showerror("ERROR", "Debe de introducir un número <= 255 y > 0")
        else:
            if (len(listaPuntos) == 0):  # Si se va a introducir el primer punto
                if(int(puntos[1].get()) <= 0):  # Si se va a introducir el primer punto y la y <= 0
                    messagebox.showerror("ERROR", "Debe de introducir un número > 0")
                else:  # Primer punto y la y != 0
                    listaPuntos.append((int(puntos[0].get()), int(puntos[1].get())))
                    cont += 1
                    puntos[2].destroy()
            elif (int(puntos[1].get()) <= listaPuntos[cont-2][1]):
                messagebox.showerror("ERROR", f"Debe de introducir un número > {listaPuntos[cont-2][1]}")
            else:
                listaPuntos.append((int(puntos[0].get()), int(puntos[1].get())))
                cont += 1
                puntos[2].destroy()
    else:
        messagebox.showerror("ERROR", "Debe de introducir un número entre 1 y 255")


def comprobarNtramos(listaDatos):

    global listaPuntos; global cont; global bIntroducirTramo; global bComprobarTramos

    listaPuntos = []; cont = 1
    nTramos = listaDatos[1].get()
    num = ["2", "3", "4", "5", "6", "7"]
    if (nTramos.isdigit()):
        if (int(nTramos) > len(num)):
             messagebox.showerror("ERROR", "Debe de introducir un número entre 2 y 7")
        else:
            print("ventana, ", cont, int(nTramos))
            bComprobarTramos.destroy()
            bIntroducirTramo = Button(listaDatos[0], text ="Introducir nuevo tramo", command= partial(nuevaVentana, [listaDatos[0], int(nTramos)]))
            bIntroducirTramo.grid(row=3, column=2)        
    else:
        messagebox.showerror("ERROR", "Debe de introducir un número entre 2 y 7")          