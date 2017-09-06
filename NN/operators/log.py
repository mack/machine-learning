from .operation import *

class log(Operation):
    def __init__(self, x):
        """ Natural logerithmic operator
        Args:
            x: Input node
        """
        super().__init__([x])

    def compute(self, x_val):
        return np.log(x_val)
