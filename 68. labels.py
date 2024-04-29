from tkinter import *


root = Tk()

photo = PhotoImage(file="teplota xd.png")

label = Label(root, text="Hello World",
              font=("Comic Sans MS", 40, "bold"),
              fg="purple",
              bg="#A09D9C",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound="bottom")
# label.place(x=0, y=0)
label.pack()

root.mainloop()