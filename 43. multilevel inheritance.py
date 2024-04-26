class Organism:
    alive = True


class Animal(Organism):

    def eat(self):
        print(f"{self.__class__.__name__} is eating")


class Dog(Animal):

    def bark(self):
        print(f"{self.__class__.__name__} is barking")


dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()
