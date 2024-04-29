from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo("OOPSIE DOOPSIE", "You have a VIRUS!!!!")
    # messagebox.showwarning("OOPSIE DOOPSIE", "You have a VIRUS!!!!")
    # messagebox.showerror("OOPSIE DOOPSIE", "You have a VIRUS!!!!")
    # if messagebox.askokcancel("Quit", "Do you want to quit?"):
    #     print("Clicked OK")
    # else:
    #     print("Clicked Cancel")
    # messagebox.askretrycancel("Retry", "Do you want to retry?")
    # messagebox.askyesno("Yes/No", "Yes or no?")
    # print(messagebox.askquestion("ask question", "do you like pie?"))  # returns string yes or no
    print(messagebox.askyesnocancel("yes no cancel", "Are you sure?"))  # returns True, False or None


root = Tk()

button = Button(root, text="Click Me!", command=click)
button.pack()

root.mainloop()
