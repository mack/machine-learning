# logistic regression on mnist instead of a superior deep convolution net
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def run():
    mnist = input_data.read_data_sets("data/", one_hot=True)
    # create variables + constants
    x = tf.placeholder(tf.float32, [None, 784])
    # start off with weights and biases at 0
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))

    y = tf.nn.softmax(tf.matmul(x,W) + b)

    y_ = tf.placeholder(tf.float32, [None, 10])
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

    sess = tf.InteractiveSession()
    for _ in range(1000):
      batch_xs, batch_ys = mnist.train.next_batch(100)
      sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})


if __name__ == '__main__':
    run()
