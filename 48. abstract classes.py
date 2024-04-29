#  abstract method has a declaration, but not an implementation
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):  # we want the user to create a more specific class - Car of Motorcycle, not just Vehicle
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):  # we must override the go method from the parent abstract class
        print("You ride the car")

    def stop(self):
        print("You stop the car")


class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")


#  vehicle = Vehicle()  I can't use this anymore, because the class is abstract
car = Car()
motorcycle = Motorcycle()

#  vehicle.go()
car.go()
motorcycle.go()
