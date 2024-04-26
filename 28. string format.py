animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)
# print(f"The {animal} jumped over the {item}")

print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item))  # positional argument
print("The {1} jumped over the {0}".format(animal, item))  # positional argument
print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))  # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal, item))
print()

name = "Bro"
print("Hello, my name is {}. Nice to meet you.".format(name))
print("Hello, my name is {:10}. Nice to meet you.".format(name))
print("Hello, my name is {:<10}. Nice to meet you.".format(name))  # left
print("Hello, my name is {:>10}. Nice to meet you.".format(name))  # right
print("Hello, my name is {:^10}. Nice to meet you.".format(name))  # center
print()

number = 3555
print("The number is {:.2f}".format(number))  # two decimal places
print("The number is {:,}".format(number))  # separate thousands
print("The number is {:b}".format(number))  # binary
print("The number is {:o}".format(number))  # octa
print("The number is {:X}".format(number))  # hexa
print("The number is {:E}".format(number))  # scientific
