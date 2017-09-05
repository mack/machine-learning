import numpy as np

class Operation(object):
    def __init__(self, input_nodes=[]):
        self.input_nodes = input_nodes
        self.consumers = [] # output nodes that recieve this operation as input_nodes

        # add this operation to all previous input nodes consumer
        for input_node in input_nodes:
            input_node.consumers.append(self)

    def compute(self):
        # implement for each specific operation
        pass
