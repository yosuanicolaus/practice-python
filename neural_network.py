import math
import random


class NeuralNetwork:
    def __init__(self, neuron_counts: list[int]) -> None:
        self.levels = [None] * (len(neuron_counts) - 1)
        for i in range(len(self.levels)):
            self.levels[i] = Level(neuron_counts[i], neuron_counts[i + 1])

    def feed_forward(self, new_inputs: list[float]) -> list[float]:
        outputs = self.levels[0].feed_forward(new_inputs)

        for i in range(1, len(self.levels)):
            outputs = self.levels[i].feed_forward(outputs)

        return outputs

    def mutate(self, mutate_power: float) -> None:
        for level in self.levels:
            level.mutate(mutate_power)

    @staticmethod
    def print_values(nn):
        i = 0
        for level in nn.levels:
            print("LEVEL", i)
            Level.print_values(level)
            i += 1


class Level:
    def __init__(self, input_count: int, output_count: int) -> None:
        self.inputs = [None for _ in range(input_count)]
        self.outputs = [None for _ in range(output_count)]
        self.biases = [None for _ in range(output_count)]
        self.weights = [[None for _ in range(
            output_count)] for _ in range(input_count)]

        for i in range(input_count):
            for o in range(output_count):
                if i == 0:
                    self.biases[o] = randgenerate()
                self.weights[i][o] = randgenerate()

    def feed_forward(self, new_inputs: list[float]) -> list[float]:
        for i in range(len(self.inputs)):
            self.inputs[i] = new_inputs[i]

        for o in range(len(self.outputs)):
            sum = 0
            for i in range(len(self.inputs)):
                sum += self.weights[i][o] * self.inputs[i]

            if o == len(self.outputs) - 1:
                self.outputs[o] = sigmoid(sum + self.biases[o])
                continue

            if sum > self.biases[o]:
                self.outputs[o] = 1
            else:
                self.outputs[o] = 0

        return self.outputs

    def mutate(self, mutate_power):
        for i in range(len(self.inputs)):
            for o in range(len(self.outputs)):
                if i == 0:
                    self.biases[o] = lerp(
                        self.biases[o],
                        randgenerate(),
                        mutate_power
                    )

                self.weights[i][o] = lerp(
                    self.weights[i][o],
                    randgenerate(),
                    mutate_power
                )

    @staticmethod
    def print_values(level):
        print("BIAS")
        print(level.biases)
        print("WEIGHTS")
        print(level.weights)


def randgenerate():
    return random.random() * 2 - 1


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def lerp(a, b, t):
    return a + (b - a) * t
