name = "Bro"  # global scope available inside and outside functions


def display_name():
    name = "Code"  # local scope available only inside this function
    print(name)


print(name)
display_name()
