def double (x):
    return x * 2


print(double(5))

double_lambda = lambda x: x * 2
print(double_lambda(5))
multiply = lambda x, y: x * y
print(multiply(5, 2))
add = lambda x, y, z: x + y + z
print(add(5, 2, 3))
full_name = lambda first, last: first + ' ' + last
print(full_name('John', 'Smith'))
age_check = lambda age: True if age >= 18 else False
print(age_check(5))