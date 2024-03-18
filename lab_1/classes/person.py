from .chromosome import Chromosome

from lab_1.utils import func, rng


class Person:
    def __init__(self, x: Chromosome, y: Chromosome, func_value: float):
        self._x = x
        self._y = y
        self._func_value = func_value

    def reduce_negative_func_value(self, min_value):
        return self._func_value + 2 * abs(min_value)

    def produce_new_people(self, other, left_b1, left_b2, h1, h2):
        y = rng.random()
        pc = rng.uniform(0.9, 1)
        if pc > y:
            x1, x2 = self.x.full_cross(other.x)
            y1, y2 = self.y.full_cross(other.y)

            p1, p2 = (Person(x1, y1, func(Chromosome.decode_number(x1.encoded, left_b1, h1),
                                          Chromosome.decode_number(y1.encoded, left_b2, h2))),
                      Person(x2, y2, func(Chromosome.decode_number(x2.encoded, left_b1, h1),
                                          Chromosome.decode_number(y2.encoded, left_b2, h2))))
        else:
            p1, p2 = Person(self.x, self.y, self.func_value), Person(other.x, other.y, other.func_value)

        p1.x.mutate()
        p1.y.mutate()
        p2.x.mutate()
        p2.y.mutate()

        p1._func_value = func(Chromosome.decode_number(p1.x.encoded, left_b1, h1),
                              Chromosome.decode_number(p1.y.encoded, left_b2, h2))
        p2._func_value = func(Chromosome.decode_number(p2.x.encoded, left_b1, h1),
                              Chromosome.decode_number(p2.y.encoded, left_b2, h2))

        return p1, p2

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
        return self.func_value > other.func_value

    def __repr__(self):
        return f'(x: {self.x}, y: {self.y}, value: {self.func_value})'
