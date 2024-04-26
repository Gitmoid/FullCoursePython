class Animal:
    alive = True

    def eat(self):
        print(f'{self.__class__.__name__} is eating')

    def sleep(self):
        print(f'{self.__class__.__name__} is sleeping')


class Rabbit(Animal):
    def run(self):
        print(f'{self.__class__.__name__} is running')


class Fish(Animal):
    def swim(self):
        print(f'{self.__class__.__name__} is swimming')


class Hawk(Animal):
    def fly(self):
        print(f'{self.__class__.__name__} is flying')


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()
hawk.fly()
