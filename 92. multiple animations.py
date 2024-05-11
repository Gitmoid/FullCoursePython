from tkinter import *
import time
from Ball import *


WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

root = Tk()

canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 4, 2, "white")
tennis_ball = Ball(canvas, 0, 0, 50, 8, 7, "yellow")
basket_ball = Ball(canvas, 0, 0, 150, 3, 1, "orange")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    root.update()
    time.sleep(0.01)

root.mainloop()
