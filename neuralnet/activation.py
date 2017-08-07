import numpy as np

def sigmoid(z, deriv=False):
    if (deriv):
        return np.multiply(z, 1-z)
    else:
        return 1.0/(1.0 + np.exp(-z))

def relu(z):
    return np.maximum(0,z)

# will add more...    
