from operation import Operation

class sigmoid(Operation):
        def __init__(self, z):
            """ Sigmoid function

            Args:
                z: Input node
            """
            super().__init__([z])

        def compute(self, z_val):
            self.inputs = [z_val]
            return 1 / (1 + np.exp(-z_val))
