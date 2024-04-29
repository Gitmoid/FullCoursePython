students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]

students.sort(reverse=True)  # only for lists [], not tuples ()
for i in students:
    print(i)
print()

sorted_students = sorted(students)
for i in sorted_students:
    print(i)
print()

students = [("Squidward", "F", 60),  # list of tuples
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78)]
grade = lambda grades: grades[1]
students.sort(key=grade)
for i in students:
    print(i[0], i[1])
print()

students = (("Squidward", "F", 60),  # tuple of tuples
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78))
age = lambda age: age[2]
sorted_students = sorted(students, key=age)
for i in sorted_students:
    print(i[0], i[2])
