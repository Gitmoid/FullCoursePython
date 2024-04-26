food = ["apple", "banana", "cherry"]
print(food)
print(food[0])

food[0] = "sushi"

food.append('orange')
food.remove("cherry")
food.pop()  # removes the last element
food.insert(0, "cake")
food.sort()  # sort alphabetically

for x in food:
    print(x)

food.clear()
