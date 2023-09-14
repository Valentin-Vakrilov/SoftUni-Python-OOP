from animal import Mammal
from ..food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    FOOD_THAT_EATS = [Vegetable, Fruit]
    FOOD_QUANTITY_PER_MEAL = 0.10

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def food_that_eats(self):
        return Mouse.FOOD_THAT_EATS

    @property
    def food_quantity_per_meal(self):
        return Mouse.FOOD_QUANTITY_PER_MEAL


class Dog(Mammal):
    FOOD_THAT_EATS = [Meat]
    FOOD_QUANTITY_PER_MEAL = 0.40

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def food_that_eats(self):
        return Dog.FOOD_THAT_EATS

    @property
    def food_quantity_per_meal(self):
        return Dog.FOOD_QUANTITY_PER_MEAL


class Cat(Mammal):
    FOOD_THAT_EATS = [Vegetable, Meat]
    FOOD_QUANTITY_PER_MEAL = 0.30

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def food_that_eats(self):
        return Cat.FOOD_THAT_EATS

    @property
    def food_quantity_per_meal(self):
        return Cat.FOOD_QUANTITY_PER_MEAL


class Tiger(Mammal):
    FOOD_THAT_EATS = [Meat]
    FOOD_QUANTITY_PER_MEAL = 1.00

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def food_that_eats(self):
        return Tiger.FOOD_THAT_EATS

    @property
    def food_quantity_per_meal(self):
        return Tiger.FOOD_QUANTITY_PER_MEAL
