from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def animal_sound(self):
        pass


class Dog(Animal):
    def animal_sound(self):
        return 'woof-woof'


class Cat(Animal):
    def animal_sound(self):
        return 'meow'


class Chicken(Animal):
    def animal_sound(self):
        return "chicken sound"


def animal_sound(animals):
    for animal in animals:
        print(animal.animal_sound())


animals = [Dog(), Cat(), Chicken()]
animal_sound(animals)
