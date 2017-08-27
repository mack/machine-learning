# logistic regression on mnist instead of a superior deep convolution net
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def main():
    mnist = input_data.read_data_sets("data/", one_hot=True)
    # create variables + constants
    x = tf.placeholder(tf.float32, [None, 784])
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.matmul(x, W) + b

    y_ = tf.placeholder(tf.float32, [None, 10])
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

    sess = tf.InteractiveSession()

    for _ in range(1):
      batch_xs, batch_ys = mnist.train.next_batch(100)

      sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})


if __name__ == '__main__':
    tf.app.run()
