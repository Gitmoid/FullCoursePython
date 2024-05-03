from tkinter import *


width = 500
height = 500
root = Tk()
root.geometry(f"{width}x{height}")

frame = Frame(root,
              bg="pink",
              bd=5,
              relief=SUNKEN,)
frame.place(x=150, y=150)

Button(frame, text="W", font=("Consolas", 25), width=3).pack(side=TOP)
Button(frame, text="S", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="A", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="D", font=("Consolas", 25), width=3).pack(side=LEFT)

root.mainloop()