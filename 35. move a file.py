import os

source = "copied_text.txt"
target_folder = "moved"
target_file = "copied_text.txt"
target = os.path.join(target_folder, target_file)

try:
    if os.path.exists(target):
        print("There is already a file there")
    else:
        if not os.path.exists(target_folder):
            os.mkdir(target_folder)
        os.replace(source, target)
        print(source+" moved successfully")
except FileNotFoundError:
    print(source+" not found")
