temp = int(input("Whats the temperature? "))

if temp >= 0 and temp <= 30:
    print("It is between 0 and 30 degrees Celsius.")
elif temp < 0 or temp > 30:
    print("Dont go outside")

if not(temp >= 0 and temp <= 30):
    print("Dont go outside")
elif not(temp < 0 or temp > 30):
    print("It is between 0 and 30 degrees Celsius.")