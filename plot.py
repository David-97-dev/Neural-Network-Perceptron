import matplotlib.pyplot as plt
import numpy as np
import math

from perceptron import perceptron


class plot:
    @staticmethod
    def plotter(synaptic_weights):

        #list = plot.get_list(synaptic_weights)
        plt.style.use('ggplot')
        plt.title('weights')
        plt.ylabel('Non-linear x')

        Xaxis = np.arange(-4, 4, 0.1)
        Yaxis = np.arange(0, 1, 0.1)
        sig = plot.sigmoid(Xaxis)
        plt.plot(Xaxis, sig, zorder=1)

        #plt.show()

    def sigmoid(x):
        a = []
        for item in x:
            a.append(1 / (1 + math.exp(-item)))
        return a
    @staticmethod
    def get_list(synaptic_weights):
        print('Normalising')
        list = []
        for weight in synaptic_weights:
            for i in weight:
                j = perceptron.sigmoid(i)
                print(j)
                list.append(j)


        return list


