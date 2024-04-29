class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")


class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")


class Person():
    def catch(self, duck_object):
        duck_object.walk()
        duck_object.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)  # the class object is less important than the methods (or attributes) walk and talk
# if Chicken didn't have the method walk or talk, the code would print an error