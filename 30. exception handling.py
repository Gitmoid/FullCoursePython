try:
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("Division by zero")
except ValueError as e:
    print(e)
    print("Please enter a number")
except Exception as e:
    print(e)
    print("Oops! Something went wrong.")
else:
    print(result)
finally:
    print("This will always execute")