import sys
import tkinter
from funciones import funciones
from principal import *
from PIL import ImageTk
from tkinter import Label, PhotoImage, Tk, Menu


def main():

    def salir():
        funciones.app.quit()

    funciones.app.geometry('1200x500')
    funciones.app['bg']='#FFFFFF'
    funciones.app.title("beta FOTOSHOP")
    label = Label(text="V I S I Ó N   P O R   C O M P U T A D O R")
    label.pack()
    label.config(fg="black", bg="#FFFFFF", font=("Helvetica 30 bold"))

    # Menu del archivo
    menuArchivo = Menu(barraMenu)
    menuArchivo.add_command(label="Abrir imagen", command=funciones.abrirImagen)
    menuArchivo.add_command(label="Guardar como", command=funciones.guardarComo)
    menuArchivo.add_command(label="Salir", command=salir)
    barraMenu.add_cascade(label="Archivo", menu=menuArchivo)

    # Menu de datos
    menuDatos = Menu(barraMenu)
    menuDatos.add_command(label="Rango valores", command=funciones.fRango)
    menuDatos.add_command(label="Info pixel", command=funciones.fInfoPixel)
    menuDatos.add_command(label="Histograma", command=funciones.fHistograma)
    menuDatos.add_command(label="Histograma Acumulado", command=funciones.fHistogramaAcumulado)
    menuDatos.add_command(label="Brillo", command=funciones.fBrillo)
    menuDatos.add_command(label="Contraste", command=funciones.fContraste)
    menuDatos.add_command(label="Entropía", command=funciones.fEntropia)
    menuDatos.add_command(label="Perfil", command=funciones.fPerfil)
    barraMenu.add_cascade(label="Datos", menu=menuDatos)


    # Menu de operaciones
    menuOperaciones = Menu(barraMenu)
    menuOperaciones.add_command(label="ROI", command=funciones.fRoi)
    menuOperaciones.add_command(label="Negativo", command=funciones.fNegativo)
    menuOperaciones.add_command(label="Ajuste lineal", command=funciones.fAjusteLineal)
    menuOperaciones.add_command(label="Transformación lineal", command=funciones.fTransformacionLineal)
    menuOperaciones.add_command(label="Corrección Gamma", command=funciones.fCorreccionGamma)
    menuOperaciones.add_command(label="Especificación del histograma", command=funciones.fEspecificacionHistograma)
    menuOperaciones.add_command(label="Ecualización del histograma", command=funciones.fEcualizacionHistograma)
    menuOperaciones.add_command(label="Diferencia", command=funciones.fDiferencia)
    menuOperaciones.add_command(label="Mapa de cambio", command=funciones.fMapaCambio)
    barraMenu.add_cascade(label="Operaciones", menu=menuOperaciones)

    
    funciones.app.config(menu=barraMenu)

main()
funciones.app.mainloop()