from machine_learning.neural_network import NeuralNetwork as nn
import random


def create_population(population_size: int, neuron_counts: list[int]) -> list[nn]:
    population = [None for _ in range(population_size)]
    for i in range(population_size):
        population[i] = nn(neuron_counts)
    return population


def fitness(nn: nn, show_values: bool = False) -> float:
    score = 0
    outputs = [None] * 4
    tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
    expectations = [0, 1, 1, 0]
    for i in range(4):
        outputs[i] = nn.feed_forward(tests[i])[0]
        score += 1 - abs(outputs[i] - expectations[i])

    if show_values:
        nn.print_values()
        print("SCORE:", score)
        print("OUTPUTS:", outputs)

    return score


# def select_pool


def main():
    structure = [2, 3, 1]
    pop_size = 250
    mutate_power = 0.1

    population = create_population(pop_size, structure)
    best_score = 0
    best_nn = None
    gen = 0

    while best_score < 3.8:
        for nn in population:
            nn_score = fitness(nn)
            if nn_score > best_score:
                best_score = nn_score
                best_nn = nn

        for i in range(pop_size):
            if i == 0:
                population[i] = best_nn
            else:
                population[i] = best_nn.copy()
                population[i].mutate(mutate_power)

        print("GEN:", gen)
        print("BEST SCORE:", best_score)
        gen += 1

    print("BEST NN:", best_nn)
    fitness(best_nn, True)


if __name__ == "__main__":
    main()
