from tkinter import *
from tkinter import filedialog
import os


def open_file():
    filepath = filedialog.askopenfilename(initialdir=os.path.dirname(os.path.abspath(__file__)),
                                          title='Open a file',
                                          filetypes=(("Text Files", "*.txt"),
                                                     ("Python Files", "*.py"),
                                                     ("All Files", "*.*"))
                                          )
    file = open(filepath, 'r')
    print(file.read())
    file.close()


root = Tk()

button = Button(root, text="open file", command=open_file)
button.pack()

root.mainloop()
