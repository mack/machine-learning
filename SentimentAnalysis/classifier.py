import re
import pickle

class Classifier(object):
    def __init__(self):
        self.positive_dict = self.load_model("positive")
        self.negative_dict = self.load_model("negative")
        self.n_positive = 0
        self.n_negative = 0

    def format_data(self):
        data = open("data/data.txt", "r")
        for idx, line in enumerate(data):
            line = line.lower()
            output = re.search(r'\d+', line).group()
            words = re.sub("[^\w]", " ",  line).split()[1:]
            self.add_to_dictionary(words, output)
        self.positive_dict = {w: v / self.n_positive for w, v in self.positive_dict.items()} # get percentages
        self.negative_dict = {w: v / self.n_negative for w, v in self.negative_dict.items()} # get percentages

    def add_to_dictionary(self, words, output):
        if output == "1":
            self.n_positive += 1
            for word in words:
                if word in self.positive_dict: # positive dictionary contains word
                    self.positive_dict[word] += 1
                else: # not found in dictionary create entry
                    self.positive_dict[word] = 1
        else:
            self.n_negative += 1
            for word in words:
                if word in self.negative_dict:
                    self.negative_dict[word] += 1
                else:
                    self.negative_dict[word] = 1

    def predict(self, input_str):
        input_str = input_str.lower()
        input_str = re.sub("[^\w]", " ",  input_str).split()

        positive_val = 1
        negative_val = 1
        for key in self.positive_dict:
            if key in input_str:
                positive_val *= self.positive_dict[key]
            else:
                positive_val *=  (1 - self.positive_dict[key])
        for key in self.negative_dict:
            if key in input_str:
                negative_val *= self.negative_dict[key]
            else:
                negative_val *=  (1 - self.negative_dict[key])

        return {"positive": positive_val, "negative": negative_val}

    def save_model(self, sent_dict, name):
        with open('data/'+ name + '.pkl', 'wb') as f:
            pickle.dump(sent_dict, f, pickle.HIGHEST_PROTOCOL)

    def load_model(self, name):
        with open('data/' + name + '.pkl', 'rb') as f:
            return pickle.load(f)
