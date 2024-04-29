from tkinter import *
from tkinter import colorchooser


def click(window):
    window.config(bg=colorchooser.askcolor()[1])

root = Tk()
root.geometry('500x500')

button = Button(root, text="Click me!", command=lambda: click(root))
button.pack()

root.mainloop()