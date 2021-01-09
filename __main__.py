from perceptron import perceptron
from plot import plot

if __name__ == "__main__":
    synaptic_weights = perceptron.run()


    plot.plotter(synaptic_weights)
