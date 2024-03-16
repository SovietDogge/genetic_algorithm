from .chromosome import Chromosome

from lab_1.utils import func


class Person:
    def __init__(self, x: Chromosome, y: Chromosome, func_value: float):
        self._x = x
        self._y = y
        self._func_value = func_value

    def reduce_negative_func_value(self, min_value):
        self._func_value += 2 * abs(min_value)

    def produce_new_people(self, other, k):
        x1, x2 = self.x.full_cross(other.x, k)
        y1, y2 = self.y.full_cross(other.y, k)
        return Person(x1, y1, func(x1.encoded, y1.encoded)), Person(x2, y2, func(x2.encoded, y2.encoded))

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def func_value(self):
        return self._func_value

    def __eq__(self, other):
        return self.func_value == other.func_value

    def __gt__(self, other):
        return self.func_value < other.func_value

    def __repr__(self):
        return f'(x: {self.x}, y: {self.y}, value: {self.func_value})'
