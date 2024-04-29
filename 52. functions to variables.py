def hello():
    print("Hello World")


print(hello)
hi = hello
print(hi)  # same memory address as hello
hi()

say = print
say("yo")
