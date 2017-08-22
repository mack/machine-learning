from classifier import *

def main():
    classifier = Classifier()
    result = classifier.predict("this was ok")
    if result['positive'] > result['negative']:
        print('positive')
    else:
        print('negative')

if __name__ == "__main__":
    main()
