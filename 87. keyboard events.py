from tkinter import *


def do_something(event):
    label.config(text=event.keysym)


root = Tk()

root.bind("<Key>", do_something)

label = Label(root, font=("Helvetice", 100))
label.pack()

root.mainloop()
