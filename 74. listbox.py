from tkinter import *


def submit():
    selected_indices = listbox.curselection()

    if not selected_indices:  # If no item is selected
        print("Please select an option to order")
        return

    food = [listbox.get(i) for i in selected_indices]

    print("You ordered", end=" ")
    for i in range(len(food)):
        if len(food) == 1:
            print(food[i])
        elif i == len(food) - 1:
            print("and", food[i])
        else:
            print(food[i], end=", ")


def add():
    if not any(char.isalpha() for char in entryBox.get()):
        print("You can't add this item to the list")
        return
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete():
    selected_indices = listbox.curselection()
    if not selected_indices:  # If no item is selected
        print("Please select an item to delete")
        return
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())


root = Tk()

listbox = Listbox(root,
                  bg="#f7ffde",
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())  # dynamically adjusts the height of the listbox based on the length of the items

entryBox = Entry(root)
entryBox.pack()

submitButton = Button(root,
                      text="submit",
                      command=submit)
submitButton.pack()

addButton = Button(root,
                   text="add",
                   command=add)
addButton.pack()

deleteButton = Button(root,
                      text="delete",
                      command=delete)
deleteButton.pack()

root.mainloop()
