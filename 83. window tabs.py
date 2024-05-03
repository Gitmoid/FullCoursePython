from tkinter import *
from tkinter import ttk


root = Tk()

notebook = ttk.Notebook(root)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

notebook.pack(expand=True, fill=BOTH)

Label(tab1, text="Hello from Tab 1", width=50, height=25).pack()
Label(tab2, text="Yo Tab 2", width=50, height=25).pack()

root.mainloop()
