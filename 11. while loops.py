name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print(f"Hello {name}")

other_name = None

while not other_name:
    other_name = input("Enter your other name: ")

print(f"Hello {other_name}")
