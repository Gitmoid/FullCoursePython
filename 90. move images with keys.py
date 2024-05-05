from tkinter import *
from import_scaled_images import import_scaled_images


root = Tk()
root.geometry('500x500')
foodImages = import_scaled_images(20, 20)

label = Label(root, image=foodImages[0])
label.place(x=0, y=0)

root.mainloop()
