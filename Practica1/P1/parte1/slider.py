import tkinter as tk
from tkinter import Scale

def valorSlider(event):
    print(k.get())

master = tk.Tk()
i = tk.Scale(master, bg="#ff0000", from_=0, to=255, orient='horizontal')
i.place(x=20, y=30)
j = tk.Scale(master, bg="#00ff00", from_=0, to=255, orient='horizontal')
j.place(x=20, y=90)
k = tk.Scale(master, bg="#0000ff", from_=0, to=255, orient='horizontal', command=valorSlider)
k.place(x=20, y=150)


master.mainloop()
