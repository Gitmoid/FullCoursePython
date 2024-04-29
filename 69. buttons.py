from tkinter import *

count = 0


def click():
    global count
    count += 1
    print(f"nice, {count}x")


root = Tk()

photo = PhotoImage(file="teplota xd.png")

button = Button(root,
                text="Clickerz",
                command=click,
                font=("Comic Sans MS", 30),
                fg="blue",
                bg="black",
                activeforeground="blue",
                activebackground="grey",
                state=ACTIVE,
                image=photo,
                compound="center")
button.pack()

root.mainloop()
