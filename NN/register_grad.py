_gradient_registry = {}

class RegisterGradient:
    def __init__(self, op_type):
        """ Creates new decorator with specific operation type
        Args:
            op_type: Name of operation
        """
        self.op_type = eval(op_type)

    def __call__(self, f):
        _gradient_registry[self.op_type] = f
        return f
