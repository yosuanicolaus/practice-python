'''
Genetic Algorithm

Objective: get parameters of foo(),
get (x, y, z) if foo(x, y ,z) equals 25
'''


import random


def foo(x, y, z):
    return 6 * x ** 3 + 9 * y ** 2 + 90 * z


def fitness(x, y, z):
    ans = foo(x, y, z) - 25

    if ans == 0:
        return 99999
    else:
        return abs(1 / ans)


def get_ranked(population):
    ranked = []
    for p in population:
        ranked.append((fitness(p[0], p[1], p[2]), p))
    ranked.sort(reverse=True)
    return ranked


def get_elements(population):
    elements = []
    for p in population:
        elements.append(p[1][0])
        elements.append(p[1][1])
        elements.append(p[1][2])
    return elements


def mutated(population):
    mutation_rate = 0.01
    for i in range(len(population)):
        if random.random() < mutation_rate:
            population[i] = random.uniform(0, 10000)
    return population


def get_new_gen(elements):
    new_gen = []
    for _ in range(1000):
        e1 = random.choice(elements) * random.uniform(0.99, 1.01)
        e2 = random.choice(elements) * random.uniform(0.99, 1.01)
        e3 = random.choice(elements) * random.uniform(0.99, 1.01)
        new_gen.append((e1, e2, e3))
    return new_gen


def main():
    population = []
    for s in range(1000):
        population.append((random.uniform(0, 10000),
                           random.uniform(0, 10000),
                           random.uniform(0, 10000)))

    for gen in range(10_000):
        ranked_population = get_ranked(population)

        print(f'Best of Generation {gen}:')
        print(f'Fitness : {ranked_population[0][0]}')
        print(f'x, y, z: {ranked_population[0][1]}')

        if ranked_population[0][0] > 100:
            x = ranked_population[0][1][0]
            y = ranked_population[0][1][1]
            z = ranked_population[0][1][2]
            print(f'result of foo: {foo(x, y, z)}')
            break

        best_population = ranked_population[:100]
        best_elements = get_elements(best_population)
        best_elements = mutated(best_elements)
        new_gen = get_new_gen(best_elements)
        population = new_gen


if __name__ == "__main__":
    main()
