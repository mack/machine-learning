from .operation import *

class reduce_sum(Operation):
    def __init__(self, A, axis=None):
        """ Natural logerithmic operator
        Args:
            A: Matrix/tensor to reduce
            axis: The axis to compute the sum (0 = rows, 1 = columns, etc)
        """
        super().__init__([A])
        self.axis = axis

    def compute(self, A_val):
        return np.sum(A_val, self.axis)
