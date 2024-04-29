from tkinter import *
from tkinter import filedialog
import os


def save_file():
    file = filedialog.asksaveasfile(initialdir=os.path.dirname(os.path.abspath(__file__)),
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text File", "*.txt"),
                                        ("HTML File", "*.html"),
                                        ("All Files", "*.*")
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0, END))  # can also use input()
    file.write(filetext)
    file.close()


root = Tk()

button = Button(root, text="save", command=save_file)
button.pack()

text = Text(root)
text.pack()

root.mainloop()
