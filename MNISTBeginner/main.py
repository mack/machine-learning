# logistic regression on mnist instead of a superior deep convolution net  
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

def run():
    load_input()
    # create variables + constants
    x = tf.placeholder(tf.float32, [None, 784])
    # start off with weights and biases at 0
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))

def load_input():
    # Load and save mnist
    mnist = input_data.read_data_sets("data/", one_hot=True)

if __name__ == '__main__':
    run()
