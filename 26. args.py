def add(*args):
    sum = 0
    # args[0] = 0  # tuple *args is ordered and unchangeable
    args = list(args)
    args[0] = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3))
