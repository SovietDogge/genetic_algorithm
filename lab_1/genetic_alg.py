from collections import namedtuple
from typing import List

import numpy as np

from classes import Person, Chromosome, func, rng

Border = namedtuple('Border', ('left', 'right'))

MIN_ITER_COUNT = 500
MIN_PERSON_COUNT = 50


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

        result.append(population[j])
        k = int(j)

    return result


def count_intervals_count(length: int) -> int:
    return 2 ** length - 1


def main():
    a_b, c_d = Border(-2, 4), Border(-4, 0)  # main func params
    l1, l2 = count_length(a_b), count_length(c_d)
    n1, n2 = count_intervals_count(l1), count_intervals_count(l2)
    h1, h2 = count_step(a_b, n1), count_step(c_d, n2)

    # a_b, c_d = Border(0, 4), Border(1, 2)  # example func params
    # l1, l2 = count_length(a_b), count_length(c_d)
    # n1, n2 = count_intervals_count(l1), count_intervals_count(l2)
    # h1, h2 = count_step(a_b, n1), count_step(c_d, n2)

    points = []
    while len(points) < MIN_PERSON_COUNT:
        ind = Border(rng.uniform(a_b.left, a_b.right), rng.uniform(c_d.left, c_d.right))
        if ind not in points:
            points.append(ind)

    population = []
    if None not in (h1, h2):
        for ind in points:
            person = Person(x=Chromosome.create_chromosome(ind.left, a_b.left, h1, l1),
                            y=Chromosome.create_chromosome(ind.right, c_d.left, h2, l2),
                            func_value=func(ind.left, ind.right))
            population.append(person)

        for _ in range(MIN_ITER_COUNT):
            min_func_value = min([person.func_value for person in population])
            if min_func_value < 0:
                fitness_func_values = [person.reduce_negative_func_value(min_func_value) for person in population]
            else:
                fitness_func_values = [person.func_value for person in population]

            fit_func_sum = sum(fitness_func_values)

            points = np.array(sorted([(value / fit_func_sum) * 100 for value in fitness_func_values]))
            circle = np.zeros(MIN_PERSON_COUNT)
            for j, _ in enumerate(points):
                circle[j] = sum(points[:j + 1])
            # TODO: Хуйня с выбором победителя
            winners = rng.random(MIN_PERSON_COUNT) * 100
            winners.sort()
            population.sort()

            new_population_parents = generate_parents_population(circle, winners, population)
            rng.shuffle(new_population_parents)

            print('Fitness sum: ', sum(person.func_value for person in population) / MIN_PERSON_COUNT)
            population.clear()
            k = rng.integers(1, min(l1, l2))

            for i in range(0, MIN_PERSON_COUNT // 2):
                parent1 = new_population_parents.pop()
                parent2 = new_population_parents.pop()
                population.extend(parent1.produce_new_people(parent2, k, a_b.left, c_d.left, h1, h2))

            best_person = sorted(population).pop()
            decoded_x = Chromosome.decode_number(best_person.x.encoded, a_b.left, h1)
            decoded_y = Chromosome.decode_number(best_person.y.encoded, c_d.left, h2)
            print(f'Best point on iteration: x: {decoded_x}, y: {decoded_y}')


if __name__ == '__main__':
    main()
