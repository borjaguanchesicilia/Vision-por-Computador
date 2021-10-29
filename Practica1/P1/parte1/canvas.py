import tkinter as tk
from PIL import Image, ImageTk

app = tk.Tk()

def main():


    #app.attributes("-fullscreen", True)
    app.geometry('1200x500')
    app['bg']='#F2F0F2'
    app.title("beta FOTOSHOP")

    #im = ImageTk.PhotoImage(Image.open("benijo.jpg").resize((415,273)))
    im = ImageTk.PhotoImage(Image.open("Tenerife.png").resize((390,265)))
    canvas = tk.Canvas(app)
    canvas.place(x=90, y=50)
    Canvas_Image = canvas.create_image(0,0, image=im, anchor="nw")


    im2 = ImageTk.PhotoImage(Image.open("benijo.jpg").resize((390,265)))
    canvas2 = tk.Canvas(app)
    canvas2.place(x=800, y=50)
    Canvas_Image2 = canvas2.create_image(0,0, image=im2, anchor="nw")

    app.mainloop()
    
main()