from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

class classifier(object):

    def __init__(self):
        self.sess = tf.InteractiveSession()

        self.x = tf.placeholder(tf.float32, [None, 784])
        self.W = tf.Variable(tf.zeros([784, 10]))
        self.b = tf.Variable(tf.zeros([10]))
        self.y = tf.nn.softmax(tf.matmul(self.x, self.W) + self.b)

        self.saver = tf.train.Saver()
        self.saver.restore(self.sess, "tmp/model.ckpt")


    def train(self):
        mnist = input_data.read_data_sets("data/", one_hot=True)

        y_ = tf.placeholder(tf.float32, [None, 10])
        cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(self.y), reduction_indices=[1]))
        train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

        tf.global_variables_initializer().run()

        for _ in range(1000):
          batch_xs, batch_ys = mnist.train.next_batch(100)
          self.sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

        self.saver.save(sess, "tmp/model.ckpt")

    def predict(self, img):
        self.sess.run(self.y, feed_dict={x: img})
        
