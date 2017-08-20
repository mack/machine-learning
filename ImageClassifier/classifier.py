import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import numpy as np

class Classifier(object):
    def __init__(self):
        self.IMG_SIZE = 50;
        self.LR = 1e-3
        self.MODEL_NAME = 'dogsvscat:{}:{}.model'.format(self.LR, '6conv-improv')

    def predict(self, image):
        model_output = self.model.predict([image])[0]
        if np.argmax(model_output) == 1: str_label = 'Dog'
        else: str_label = 'Cat'
        certainty = model_output[np.argmax(model_output)] * 100
        model_output_dict = {'prediction':str_label, 'prediction_val': certainty}
        return model_output_dict

    def load_model(self):
        convnet = input_data(shape=[None, self.IMG_SIZE, self.IMG_SIZE, 1], name='input')
        convnet = conv_2d(convnet, 32, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)
        convnet = conv_2d(convnet, 64, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)
        convnet = conv_2d(convnet, 128, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)
        convnet = conv_2d(convnet, 64, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)
        convnet = conv_2d(convnet, 32, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)
        convnet = fully_connected(convnet, 1024, activation='relu')
        convnet = dropout(convnet, 0.8)
        convnet = fully_connected(convnet, 2, activation='softmax')
        convnet = regression(convnet, optimizer='adam', learning_rate=self.LR, loss='categorical_crossentropy', name='targets')

        self.model = tflearn.DNN(convnet, tensorboard_dir='log')

        self.model.load('dogvcat-dnn-classifier.tfl') # accidentally added the .meta, whoops


    # def train(self):
    #     train_data = np.load('train_data.npy')
    #
    #     train = train_data[:-500]
    #     test = train_data[-500:]
    #
    #     X = np.array([i[0] for i in train]).reshape(-1, self.IMG_SIZE, self.IMG_SIZE, 1)
    #     Y = [i[1] for i in train]
    #
    #     test_x = np.array([i[0] for i in test]).reshape(-1, self.IMG_SIZE, self.IMG_SIZE,1)
    #     test_y = [i[1] for i in test]
    #
    #     self.model.fit({'input': X}, {'targets': Y}, n_epoch=10, validation_set=({'input': test_x}, {'targets': test_y}), snapshot_step=500, show_metric=True, run_id=self.MODEL_NAME)
    #     self.model.save('dogvcat-dnn-classifier.tfl')
