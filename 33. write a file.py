text = "w will overwrite the file\na will not overwrite the file, it will append"

with open("text.txt", "a") as f:
    f.write(text)
