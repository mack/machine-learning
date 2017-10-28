import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import plotly.plotly as py
import plotly
from plotly.graph_objs import *

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
    def compress_with_eigen(self,size):
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
        matrix_w = np.hstack([eig_pairs[i][1].reshape(4,1) for i in range(size)])
        return self.tensor.dot(matrix_w)


    def compress_with_SVD(self):
        U,S,V = np.linalg.svd(self.tensor.T)


def main():
    # load in the iris dataset
    dataframe = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
    dataframe.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
    X = dataframe.iloc[:,0:4].values
    y = dataframe.iloc[:,4].values
    # _X now has 2 dimensions....
    _X = PCA(X).compress_with_eigen(2)

    # display data
    traces = []
    for name in ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'):
        trace = Scatter(
            x=_X[y==name,0],
            y=_X[y==name,1],
            mode='markers',
            name=name,
            marker=Marker(
                size=12,
                line=Line(
                    color='rgba(217, 217, 217, 0.14)',
                    width=0.5),
                opacity=0.8))
        traces.append(trace)

    data = Data(traces)
    layout = Layout(xaxis=XAxis(title='PC1', showline=False),
                    yaxis=YAxis(title='PC2', showline=False))
    fig = Figure(data=data, layout=layout)
    plotly.offline.iplot(fig)






if __name__ == '__main__':
    plotly.offline.init_notebook_mode(connected=True)
    main()
