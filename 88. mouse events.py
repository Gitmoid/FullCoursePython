from tkinter import *


def do_something(event):
    print(f"Mouse coordinates: {event.x}, {event.y}")


root = Tk()

root.bind("<Button-1>", do_something)
root.bind("<ButtonRelease-3>", do_something)
root.bind("<Enter>", do_something)
root.bind("<Leave>", do_something)
root.bind("<Motion>", do_something)

root.mainloop()
