import re

class Classifier(object):
    def __init__(self):
        self.positive_dict = {}
        self.negative_dict = {}
        self.n_positive = 0
        self.n_negative = 0
        self.format_data()

    def format_data(self):
        data = open("data/data.txt", "r")
        for idx, line in enumerate(data):
            output = re.search(r'\d+', line).group()
            words = re.sub("[^\w]", " ",  line).split()[1:]
            self.add_to_dictionary(words, output)
        self.positive_dict = {w: v / self.n_positive for w, v in self.positive_dict.items()} # get percentages
        self.negative_dict = {w: v / self.n_negative for w, v in self.negative_dict.items()} # get percentages
        print(self.positive_dict)

    def add_to_dictionary(self, words, output):
        if output == "1":
            self.n_positive += 1
            for word in words:
                word = word.lower()
                if word in self.positive_dict: # positive dictionary contains word
                    self.positive_dict[word] += 1
                else: # not found in dictionary create entry
                    self.positive_dict[word] = 1
        else:
            self.n_negative += 1
            for word in words:
                word = word.lower()
                if word in self.negative_dict:
                    self.negative_dict[word] += 1
                else:
                    self.negative_dict[word] = 1
