from tkinter import *


def submit():
    print(text.get(1.0, END))


root = Tk()

text = Text(root,
            bg="light yellow",
            fg="black",
            font=("Ink Free", 25),  # the area of the window corresponds to the font size
            height=8,  # it can fit 8 characters now
            width=20,
            padx=20,
            pady=20)
text.pack()

button = Button(root, text="submit", command=submit)
button.pack()

root.mainloop()
