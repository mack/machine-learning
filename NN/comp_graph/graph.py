class Graph(object):

    def __init__(self):
        self.operations = []
        self.placeholders = []
        self.variables = []

        def as_default(self):
            global _default_graph
            _default_graph = self
