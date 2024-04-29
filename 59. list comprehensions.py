squares = []
for i in range(1, 11):
    squares.append(i*i)
print(squares)

squares_comprehensions = [i * i for i in range(1, 11)]
print(squares_comprehensions)

students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 0]

passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

passed_students_comprehensions = [i for i in students if i >= 60]
print(passed_students_comprehensions)

passed_students_comprehensions = [i if i >= 60 else "FAILED" for i in students]
print(passed_students_comprehensions)
