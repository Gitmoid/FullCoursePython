from tkinter import *


def display():
    if x.get():
        print("You agree")
    else:
        print("You dont agree")


root = Tk()

# x = IntVar()   when on/off is 1 and 0
# x = StringVar()  when on/off are strings (yes/no)
x = BooleanVar()

photo = PhotoImage(file="teplota xd.png")

check_button = Checkbutton(root,
                           text="I agree",
                           variable=x,
                           onvalue=True,  # by default 1
                           offvalue=False,
                           command=display,
                           font=("Comic Sans MS", 20),
                           fg="blue",
                           bg="black",
                           activeforeground="purple",
                           activebackground="black",
                           padx=25,
                           pady=10,
                           image=photo,
                           cursor="hand2",
                           compound="bottom")
check_button.pack()

root.mainloop()
