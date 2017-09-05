from session import *

""" Perceptron test w/ softmax
Testing a simply linear classifier using made up data.

Written: Tue, Sept. 5th 2017
Author: Mackenzie Boudreau
References: http://www.deepideas.net/deep-learning-from-scratch-theory-and-implementation/

"""

def main():
    red = np.random.randn(50, 2) - (2 * np.ones((50,2)))
    blue = np.random.randn(50, 2) - (2 * np.ones((50,2)))

    Graph().as_default()

    x = placeholder()
    w = Variable([1, 1])
    b = Variable(0)
    #

if __name__ == '__main__':
    main()
