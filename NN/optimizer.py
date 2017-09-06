from operators.operation import *
from queue import Queue

class GradientDescentOptimizer:
    def __init__(self, LR):
        self.learning_rate = LR

    def minimize(self, loss):
        learning_rate = self.learning_rate
        class MinimizeOperation(Operation):
            def compute(self):
                grad_table = compute_gradients(loss)

                for node in grad_table:
                    if type(node) == Variable:
                        grad = grad_table[node]
                        node.value -= learning_rate * grad
        return MinimizeOperation()
