while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "555-555-5555"

for i in phone_number:
    if i == "-":
        continue  # end current loop here and start a new one
    print(i, end="")

print()

for i in range(1, 21):
    if i == 13:
        pass  # continues the loop
    else:
        print(i, end=" ")
    print("is a number")
