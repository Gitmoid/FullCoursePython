import random

x = random.randint(1, 100)
y = random.random()

myList = ["rock", "paper", "scissors"]
z = random.choice(myList)

cards = list(range(2, 10)) + ["J", "Q", "K", "A"]
random.shuffle(cards)

print(x, y, z)
print(cards)