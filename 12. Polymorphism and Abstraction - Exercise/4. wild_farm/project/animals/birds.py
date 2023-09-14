from .animal import Bird
from food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    FOOD_THAT_EATS = [Meat]
    FOOD_QUANTITY_PER_MEAL = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def food_that_eats(self):
        return Owl.FOOD_THAT_EATS

    @property
    def food_quantity_per_meal(self):
        return Owl.FOOD_QUANTITY_PER_MEAL


class Hen(Bird):
    FOOD_THAT_EATS = [Vegetable, Fruit, Meat, Seed]
    FOOD_QUANTITY_PER_MEAL = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def food_that_eats(self):
        return Hen.FOOD_THAT_EATS

    @property
    def food_quantity_per_meal(self):
        return Hen.FOOD_QUANTITY_PER_MEAL
