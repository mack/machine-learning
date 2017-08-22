import re

class Classifier(object):
    def __init__(self):
        self.format_data()

    def format_data(self):
        data = open("data/data.txt", "r")
        positive = open("data/positive.txt", "w")
        negative = open("data/negative.txt", "w")
        for idx, line in enumerate(data):
            if idx == 0:
                output = re.search(r'\d+', line).group()
                if output == 1:
