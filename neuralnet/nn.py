import numpy as np

class NeuralNet:
    # basic two layer nn
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        self.weights = np.random.rand()



    def train(self):
