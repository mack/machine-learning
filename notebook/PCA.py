import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls

class PCA(object):
    def __init__(self, tensor):
        tensor_std = StandardScaler().fit_transform(tensor);
        self.tensor = tensor_std

    """ Compress
    Using eigenvalue decomposition to perform principle component analysis.
    (demonsionality reduction)
    args:
        array: n x m array, to Compress
    return:

    """
    def compress_with_eigen(self):
        # feature scaling (standardize data)
        # covariance matrix
        tensor_covar = np.cov(self.tensor.T)
        # eigen decomposition
        eig_values, eig_vectors = np.linalg.eig(tensor_covar)

        # drop lowest rated eigen vectors
        eig_pairs = [(np.abs(eig_values[i]), eig_vectors[:, i]) for i in range(len(eig_values))]

        # sort in descending order
        eig_pairs.sort()
        eig_pairs.reverse()

        # construct projection matrix
        matrix_w = np.hstack((eig_pairs[0][1].reshape(4,1),
                      eig_pairs[1][1].reshape(4,1)))
        return self.tensor.dot(matrix_w)


    def compress_with_SVD(self):
        U,S,V = np.linalg.svd(self.tensor.T)


def main():
    # np.random.seed(0)
    # x = np.random.rand(4,3) * 10
    # x[0,0] = 1000
    # x[0, 1] = 500
    #
    #
    # print(x)
    # y = np.random.rand(4) * 25
    # y[0] =100
    # print(y)
    # plt.plot(x, y, 'ro')
    # plt.show()

    # load in the iris dataset
    dataframe = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
    dataframe.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
    X = dataframe.iloc[:,0:4].values
    y = dataframe.iloc[:,4].values
    _X = PCA(X).compress_with_eigen()


if __name__ == '__main__':
    main()
