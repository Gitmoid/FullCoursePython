rows = int(input("How many rows? "))
cols = int(input("How many columns? "))
symbol = input("Enter a symbol: ")

for row in range(rows):
    for col in range(cols):
        print(symbol, end=" ")
    print()