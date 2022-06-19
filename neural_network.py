import random


class NeuralNetwork:
    def __init__(self, neuron_counts: list[int]) -> None:
        self.levels = [None] * (len(neuron_counts) - 1)
        for i in range(len(self.levels)):
            self.levels[i] = Level(neuron_counts[i], neuron_counts[i + 1])

    @staticmethod
    def print_values(nn):
        i = 0
        for level in nn.levels:
            print("LEVEL", i)
            Level.print_values(level)
            i += 1


class Level:
    def __init__(self, input_count: int, output_count: int) -> None:
        self.inputs = [None] * input_count
        self.outputs = [None] * output_count
        self.biases = [None] * output_count
        self.weights = [[None] * output_count] * input_count

        for i in range(input_count):
            for o in range(output_count):
                if i == 0:
                    self.biases[o] = random.random() * 2 - 1
                self.weights[i][o] = random.random() * 2 - 1

    @staticmethod
    def print_values(level):
        print("BIAS")
        print(level.biases)
        print("WEIGHTS")
        print(level.weights)
