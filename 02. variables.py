first_name: str = "Bro"
last_name: str = "Code"
full_name: str = first_name + " " + last_name
print("Hello " + first_name)
print(f"Class of {first_name} is {str(type(first_name))}")
print(f"Class of {full_name} is {str(type(full_name))}")

age = 68
age += 1
print(age)
print("Your age is: " + str(age))
print(f"Class of {age} is {str(type(age))}")

height = 250.5
print(height)
print(f"Class of {height} is {str(type(height))}")

human = False
print(human)
print(f"Class of {human} is {str(type(human))}")
