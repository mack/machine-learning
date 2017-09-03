from operation import Operation

class subtract(Operation):
    def __init__(self, x, y):
        """ element-wise subtraction

        Args:
            x: First node
            y: second node
        """
        super().__init__([x, y])

    def compute(self, x_val, y_val):
        self.inputs = [x_val, y_val]
        return x_val - y_val
