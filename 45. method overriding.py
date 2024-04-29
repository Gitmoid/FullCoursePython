class Animal:

    def eat(self):
        print("Animal is eating")


class Rabbit(Animal):

    def eat(self):  # method signature
        print("Rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()
