from graph import *

class placeholder(object):
    """
    Represents a placeholder input node
    thats provided a value when computing output of a graph
    """

    def __init__(self):
        self.consumers = []
        # add to global var _default_graph
        _default_graph.placeholders.append(self)

class Variable(object):
    """
    Represents a variable or changable input value.
    """

    def __init__(self, init_value = None):
        self.value = init_value
        self.consumers = []

        _default_graph.variables.append(self)
