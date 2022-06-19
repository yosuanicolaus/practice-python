from neural_network import NeuralNetwork as nn


def main():
    brain = nn([2, 4, 1])
    nn.print_values(brain)


if __name__ == "__main__":
    main()
