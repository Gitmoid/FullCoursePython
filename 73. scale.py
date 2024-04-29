from tkinter import *


root = Tk()

scale = Scale(root,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=("Consolas", 20),
              tickinterval=10,
              # showvalue=0)  # hide current value
              resolution=.00005,
              troughcolor='brown',
              fg="black",
              bg="gray")
scale.set((abs(scale['from']) + abs(scale['to'])) / 2)  # start the scale in the middle
scale.pack()

button = Button(root,
                text="submit",
                command=lambda: print("The temperature is", scale.get(), "°C"))
button.pack()

root.mainloop()
