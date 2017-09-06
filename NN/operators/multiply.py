from .operation import *

class mulyiply(Operation):
    def __init__(self, x1, x2):
        """ Element wise multiplication on two matrices
        Args:
            x1: First matrix
            x2: Second matrix
        """
        super().__init__([x1, x2])

    def compute(self, x1_val, x2_val):
        return np.multiply(x1_val, x2_val)
