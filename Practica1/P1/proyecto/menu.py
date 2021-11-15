from funciones import *
from PIL import ImageTk
from tkinter import Label


def main():

    def salir():
        app.quit()

    app.geometry('1200x500')
    app['bg']='#FFFFFF'
    app.title("beta FOTOSHOP")
    label = Label(text="V I S I Ó N   P O R   C O M P U T A D O R")
    label.pack()
    label.config(fg="black", bg="#FFFFFF", font=("Helvetica 30 bold"))

    # Menu del archivo
    menuArchivo = tk.Menu(barraMenu)
    menuArchivo.add_command(label="Abrir imagen", command=abrirImagen)
    menuArchivo.add_command(label="Guardar", command=guardar)
    menuArchivo.add_command(label="Guardar como", command=guardarComo)
    menuArchivo.add_command(label="Salir", command=salir)
    barraMenu.add_cascade(label="Archivo", menu=menuArchivo)

    # Menu de datos
    menuDatos = tk.Menu(barraMenu)
    menuDatos.add_command(label="Rango valores", command=fRango)
    menuDatos.add_command(label="Info pixel", command=fInfoPixel)
    menuDatos.add_command(label="Histograma", command=fHistograma)
    menuDatos.add_command(label="Histograma Acumulado", command=fHistogramaAcumulado)
    menuDatos.add_command(label="Brillo", command=fBrillo)
    menuDatos.add_command(label="Contraste", command=fContraste)
    menuDatos.add_command(label="Entropía", command=fEntropia)
    barraMenu.add_cascade(label="Datos", menu=menuDatos)


    # Menu de operaciones
    menuOperaciones = tk.Menu(barraMenu)
    menuOperaciones.add_command(label="ROI", command=fRoi)
    menuOperaciones.add_command(label="Negativo", command=fNegativo)
    menuOperaciones.add_command(label="Transformación lineal", command=fTransformacionLineal)
    menuOperaciones.add_command(label="Corrección Gamma", command=fCorreccionGamma)
    menuOperaciones.add_command(label="Especificación del histograma", command=fEspecificacionHistograma)
    menuOperaciones.add_command(label="Ecualización del histograma", command=fEcualizacionHistograma)
    barraMenu.add_cascade(label="Operaciones", menu=menuOperaciones)

    
    app.config(menu=barraMenu)

main()
app.mainloop()