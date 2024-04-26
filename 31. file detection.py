import os

filename = "text.txt"
dirname = "folder"
# dirname = os.path.dirname(__file__)
# filename = os.path.join(dirname, path)

if os.path.exists(filename):
    print("Location exists")
    if os.path.isfile(filename):
        print("File exists")
    if os.path.isdir(dirname):
        print("Directory exists")