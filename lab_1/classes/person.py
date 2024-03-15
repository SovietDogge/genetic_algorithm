from .chromosome import Chromosome


class Person:
    def __init__(self, x: Chromosome, y: Chromosome, func_value: float):
        self._x = x
        self._y = y
        self._func_value = func_value

    def reduce_negative_func_value(self, min_value):
        self._func_value += 2 * abs(min_value)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def func_value(self):
        return self._func_value

    def __repr__(self):
        return f'(x: {self.x}, y: {self.y}, value: {self.func_value})'
