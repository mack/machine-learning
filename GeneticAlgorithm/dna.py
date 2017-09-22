import random
import string

class DNA(object):

    def __init__(self, length):
        self.length = length
        self.data = self.random_by_length()
        self.score = 0

    def random_by_length(self):
        d = []
        for i in range(self.length):
            random_char = random.choice(string.ascii_letters + " ")
            d.append(random_char)
        return d

    def rate(self, target):
        for i in range(self.length):
            if self.data[i] == target[i]:
                self.score += 1
        return self.score
