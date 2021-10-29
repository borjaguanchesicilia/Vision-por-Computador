from funciones import *

def main():

    def salir():
        app.quit()

    #app.attributes("-fullscreen", True)
    app.geometry('1200x500')
    app['bg']='#FFFFFF'
    app.title("beta FOTOSHOP")

    barraMenu = tk.Menu(app)

    # Menu del archivo
    menuArchivo = tk.Menu(barraMenu)
    menuArchivo.add_command(label="Abrir imagen", command=abrirImagen)
    menuArchivo.add_command(label="Guardar", command=guardar)
    menuArchivo.add_command(label="Guardar como", command=guardarComo)
    menuArchivo.add_command(label="Salir", command=salir)
    barraMenu.add_cascade(label="Archivo", menu=menuArchivo)

    # Menu de herramienta
    menuHerramientas = tk.Menu(barraMenu)
    menuHerramientas.add_command(label="Histograma", command=fHistograma)
    menuHerramientas.add_command(label="Brillo", command=fBrillo)
    menuHerramientas.add_command(label="Contraste", command=fContraste)
    barraMenu.add_cascade(label="Herramientas", menu=menuHerramientas)

    app.config(menu=barraMenu)

    label = Label(text="F O T O S H O P")
    label.pack()
    label.config(fg="black", bg="#1469BE", font=("Helvetica 30 bold"))

    app.mainloop()

main()