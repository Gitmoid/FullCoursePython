from tkinter import *


def create_window():
    new_window = Tk()  # if main window closes, this closes as well. Tk() will stay
    root.destroy()


root = Tk()

Button(root, text="create new window", command=create_window).pack()

root.mainloop()
