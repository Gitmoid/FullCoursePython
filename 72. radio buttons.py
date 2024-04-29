from tkinter import *
from PIL import Image, ImageTk  # resizing images


def order():
    if(x.get()==0):
        print("You ordered an apple")
    elif(x.get()==1):
        print("You ordered an orange")
    elif(x.get()==2):
        print("You ordered a banana")
    else:
        print("huh?")

root = Tk()

# width = 50
# height = 50
#
# food = ['apple', 'orange', 'banana']
# appleImage = Image.open('apple.png')
# orangeImage = Image.open('orange.png')
# bananaImage = Image.open('banana.png')
# resized_apple = appleImage.resize((width, height))
# appleImg = ImageTk.PhotoImage(resized_apple)
# resized_orange = orangeImage.resize((width, height))
# orangeImg = ImageTk.PhotoImage(resized_orange)
# resized_banana = bananaImage.resize((width, height))
# bananaImg = ImageTk.PhotoImage(resized_banana)
# foodImages = [appleImg, orangeImg, bananaImg]

width = 75
height = 75

food = ['apple', 'orange', 'banana']
foodImages = []

for item in food:
    image = Image.open(f'{item}.png')
    resized_image = image.resize((width, height))
    foodImg = ImageTk.PhotoImage(resized_image)
    foodImages.append(foodImg)

x = IntVar(value=-1)    # value=-1 prevents the button from appearing clicked when program is launched,
                        # as the default value of x is 0, as is the value of the first button

for i in range(len(food)):
    radio_button = Radiobutton(root,
                               text=food[i],
                               variable=x,  # groups radiobuttons together if they share the same variable
                               value=i,     # assigns each radiobutton a different value
                               padx=25,
                               font=("Impact", 50),
                               image=foodImages[i],
                               compound=RIGHT,
                               cursor="hand2",
                               indicatoron=0,
                               width=400,
                               command=order)  # eliminate circle indicator
    radio_button.pack(anchor=W)

root.mainloop()
