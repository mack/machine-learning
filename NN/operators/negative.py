from .operation import *

class negative(Operation):
    def __init__(self, x):
        """ Element wise negative on operator
        Args:
            x: Input node
        """
        super.__init__([x])

    def compute(self, x_val):
        return -x_val
