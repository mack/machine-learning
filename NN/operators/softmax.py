from .operation import *

class softmax(Operation):
    def __init__(self, a):
        """
        Args:
            a: Input node
        """
        super().__init__([a])

    def compute(self, a_val):
        return np.exp(a_val) / np.sum(np.exp(a_val), axis=1)[:, None]
