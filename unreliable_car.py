"""Github Link - https://github.com/WilliamLynn2002/Practical8/blob/master/unreliable_car.py"""

from car import Car
from random import randint


class UnreliableCar(Car):
    """An unreliable version of a car."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        total_distance = super().drive(distance)
        return total_distance
