f = None
try:
    with open("text.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")

if f is not None:
    print(f.closed)  # with open automatically closes files, but doesn't catch errors
