from PIL import Image, ImageTk  # resizing images


def import_scaled_images(width, height):
    w = width
    h = height

    food = ['apple', 'orange', 'banana']
    foodImages = []

    for item in food:
        image = Image.open(f'{item}.png')
        resized_image = image.resize((w, h))
        foodImg = ImageTk.PhotoImage(resized_image)
        foodImages.append(foodImg)
    return foodImages