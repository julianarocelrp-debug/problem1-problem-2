class Car:
    def move(self):
        print("The car is driving!")


class Person:
    def move(self):
        print("The person is walking!")


class Robot:
    def move(self):
        print("The robot is moving!")


def make_it_move(thing):
    thing.move()


car = Car()
person = Person()
robot = Robot()

things = [car, person, robot]


for thing in things:
    make_it_move(thing)
