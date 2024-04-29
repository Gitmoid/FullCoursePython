happy = True
print(happy)

print(happy := False)

foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

while food := input("What food do you like?: ") != "quit":
    foods.append(food)
