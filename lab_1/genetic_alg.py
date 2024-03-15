from collections import namedtuple
from typing import List

import numpy as np

from classes import Person, Chromosome

rng = np.random.default_rng(12)

Border = namedtuple('Border', ('left', 'right'))

MIN_ITER_COUNT = 500
MIN_PERSON_COUNT = 50


def func(x, y):
    return abs(x) + y


def count_length(borders: Border, q: int = 1) -> int:
    return np.ceil(np.log2((borders.right - borders.left) * 10 ** q + 1))


def count_step(borders: Border, n: int, e: float = 0.1) -> float | None:
    h = (borders.right - borders.left) / n
    return h if h <= e else None


def generate_parents_population(points: np.array, winners: np.array, population: List[Person]):
    k = 0
    result = []
    for i in range(0, MIN_PERSON_COUNT):
        for j in (range(k, MIN_PERSON_COUNT)):
            if winners[i] < points[j]:
                break

        result.append(population[i])
        k = int(j)

    return result


def count_intervals_count(length: int) -> int:
    return 2 ** length - 1


def main():
    # example = Borders(-1, 2)
    a_b, c_d = Border(-2, 4), Border(-4, 0)
    l1, l2 = count_length(a_b), count_length(c_d)
    n1, n2 = count_intervals_count(l1), count_intervals_count(l2)
    h1, h2 = count_step(a_b, n1), count_step(c_d, n2)

    points = []
    while len(points) < MIN_PERSON_COUNT:
        ind = Border(rng.uniform(-2, 4), rng.uniform(0, 4))
        if ind not in points:
            points.append(ind)

    population = []
    if None not in (h1, h2):
        for ind in points:
            person = Person(x=Chromosome.create_chromosome(ind.left, a_b.left, h1),
                            y=Chromosome.create_chromosome(ind.right, c_d.left, h2),
                            func_value=func(ind.left, ind.right))
            population.append(person)

        for _ in range(MIN_ITER_COUNT):
            min_func_value = min([person.func_value for person in population])
            if min_func_value < 0:
                _ = [person.reduce_negative_func_value(min_func_value) for person in population]
            fit_func_sum = sum([person.func_value for person in population])

            points = np.array(sorted([(person.func_value / fit_func_sum) * 100 for person in population]))
            circle = np.zeros(MIN_PERSON_COUNT)
            for j, _ in enumerate(points):
                circle[j] = sum(points[:j + 1])

            winners = rng.random(50) * 100
            winners.sort()

            new_population_parents = generate_parents_population(circle, winners, population)
            k = rng.integers(0, min(l1, l2))





        print(circle)
        print(winners)
        print(new_population_parents)


if __name__ == '__main__':
    main()
