from tkinter import *
import time
from import_scaled_images import import_scaled_images


WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

root = Tk()
foodImages = import_scaled_images(100, 100)

canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

photo_image = foodImages[0]
my_image = canvas.create_image(0, 0, anchor=NW, image=photo_image)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    if (coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0):
        xVelocity = -xVelocity
    if (coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0):
        yVelocity = -yVelocity
    canvas.move(my_image, xVelocity, yVelocity)
    root.update()
    time.sleep(0.01)

root.mainloop()
