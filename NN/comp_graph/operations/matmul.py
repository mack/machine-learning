from operation import Operation

class matmul(Operation):
    def __init__(self, x1, x2):
        """ Matrix multiplication

        Args:
            x1: First matrix
            x2: Second matrix
        """
        super().__init__([x1, x2])

    def compute(self, x1_val, x2_val):
        self.inputs = [x1_val, x2_val]
        return x1_val.dot(x2_val)
