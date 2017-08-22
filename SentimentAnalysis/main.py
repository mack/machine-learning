from classifier import *

def main():
    classifier = Classifier()
    result = classifier.predict("this was the best")
    if result['positive'] > result['negative']:
        percentage_pos = result['positive'] / (result['positive'] + result['negative'])
        print("Positive: " + str(percentage_pos) + "%")
    else:
        percentage_neg = result['negative'] / (result['positive'] + result['negative'])
        print("Negative: " + str(percentage_neg) + "%")

if __name__ == "__main__":
    main()
