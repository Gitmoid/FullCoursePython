from tkinter import *


root = Tk()

titleLabel = Label(root, text="Enter your info", font=("Arial", 25)).grid(row=0, column=0, columnspan=2)

firstNameLabel = Label(root, text="First name: ", width=20, bg="red").grid(row=1, column=0)
firstNameEntry = Entry(root).grid(row=1, column=1)

lastNameLabel = Label(root, text="Last name: ", bg="green").grid(row=2, column=0)
lastNameEntry = Entry(root).grid(row=2, column=1)

emailNameLabel = Label(root, text="Email: ", bg="blue").grid(row=3, column=0)
emailNameEntry = Entry(root).grid(row=3, column=1)

submitButton = Button(root, text="Submit").grid(row=4, column=0, columnspan=2)

root.mainloop()
