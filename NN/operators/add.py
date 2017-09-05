from .operation import *

class add(Operation):
    def __init__(self, x, y):
        """ returns element-wise addition

        Args:
        x: First nodes
        y: Second node
        """
        super().__init__([x, y])

    def compute(self, x_val, y_val):
        self.inputs = [x_val, y_val]
        return x_val + y_val
