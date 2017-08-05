import numpy as np

def square_error(x, y, deriv):
    if (deriv):
        return (x - y)
    else:
        return 0.5 * np.mean(np.sum(np.power(x - y, 2), axis=1))
