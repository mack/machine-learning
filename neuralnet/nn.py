import numpy as np
from activation import *

class Network(object):
    # First test: making a basic 2 layer
    def __init__(self):
        self.w1 = np.random.randn(4, 8);
        self.w2 = np.random.randn(8, 1);

    def feed_forward(self, x):
        # store for later usage
        self.z1 = x.dot(self.w1);
        self.a1 = sigmoid(z1);
        self.z2 = a1.dot(w2);
        self.a2 = sigmoid(w2)
        return a2;

    def back_prop(self, x, y):
        # function should return a gradient matrix for both dC/dW1 & dC/dW2
        y_ = feed_forward(x); # to set up variables

        # compute delta for output layer to use in next backprop
        delta2 = (y_ - y) * sigmoid(self.z2, deriv=True);
        # compute gradient matrix
        dCdW2 = delta2.dot(self.a1);

        # Propagate error further backwards
        delta1 = dCdW2.dot(self.w1) * sigmoid(self.z1, deriv=True);
        dCdW1 = x.dot(delta1);

        return dCdW1, dCdW2

        
