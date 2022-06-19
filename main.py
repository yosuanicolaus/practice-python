from neural_network import NeuralNetwork as nn


def main():
    brain = nn([2, 4, 1])
    nn.print_values(brain)

    outputs = brain.feed_forward([3, 5])
    print("outputs", outputs)
    outputs = brain.feed_forward([1, 2])
    print("outputs", outputs)

    brain.mutate(0.1)
    print("mutated")
    nn.print_values(brain)


if __name__ == "__main__":
    main()
