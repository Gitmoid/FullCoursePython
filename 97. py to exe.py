from tkinter import *
from time import *


def update():
    time_string = strftime("%H:%M:%S", localtime())
    time_label.config(text=time_string)

    day_string = strftime("%A", localtime())
    day_label.config(text=day_string)

    date_string = strftime("%d. %b %Y", localtime())
    date_label.config(text=date_string)

    root.after(1000, update)
    # time_label.after(1000, update)


root = Tk()

time_label = Label(root, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack()

day_label = Label(root, font=("Ink Free", 25))
day_label.pack()

date_label = Label(root, font=("Ink Free", 30))
date_label.pack()

update()

root.mainloop()

# pyinstaller -F -w "97. py to exe.py"
