from tkinter import *
from import_scaled_images import import_scaled_images


def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 10)  # canvas.move(foodImages[0], 0, -10)

def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 10)


def move_left(event):
    label.place(x=label.winfo_x() - 10, y=label.winfo_y())


def move_right(event):
    label.place(x=label.winfo_x() + 10, y=label.winfo_y())


root = Tk()
root.geometry('500x500')
foodImages = import_scaled_images(20, 20)

root.bind("<w>", move_up)
root.bind("<s>", move_down)
root.bind("<a>", move_left)
root.bind("<d>", move_right)

label = Label(root, image=foodImages[0])  # same with canvas
label.place(x=0, y=0)

root.mainloop()
