from tkinter import *
from import_scaled_images import import_scaled_images


def open_file():
    print("Opening file...")


def save_file():
    print("Saving file...")


def cut():
    print("Cutting...")


def copy():
    print("Copying...")


def paste():
    print("Pasting...")


root = Tk()

foodImages = import_scaled_images(20, 20)

menubar = Menu(root)
root.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label="Open", command=open_file, image=foodImages[0], compound=LEFT)
fileMenu.add_command(label="Save", command=save_file, image=foodImages[1], compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit, image=foodImages[2], compound=LEFT)

editMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

root.mainloop()
