import numpy as np


class perceptron:
    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def sigmoid_derivative(x):
        return x * (1 - x)


    @staticmethod
    def run():

        training_inputs = np.array([[0,0,1],
                                   [1,1,1],
                                   [1,0,1],
                                   [0,1,1]])

        training_outputs = np.array([[0,2,2,0]]).T

        np.random.seed(1)

        synaptic_weights = 2 * np.random.random((3,1)) - 1

        print('Random starting synaptic weights: ')
        print(synaptic_weights)

        for iteration in range(50000):
            input_layer = training_inputs

            outputs = perceptron.sigmoid(np.dot(input_layer, synaptic_weights))

            error = training_outputs - outputs

            adjustments = error * perceptron.sigmoid_derivative(outputs)

            synaptic_weights += np.dot(input_layer.T, adjustments)

        print('Synaptic weights after training')
        print(synaptic_weights)

        print('Outputs after training')
        print(outputs)
