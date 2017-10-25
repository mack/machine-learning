import numpy
from sklearn.preprocessing import StandardScaler

class PCA(object):
    def __init__(self):
        pass;
    """ Compress
    Using eigenvalue decomposition to perform principle component analysis.
    (demonsionality reduction)
    args:
        array: n x m array, to Compress
    return:

    """
    def compress_with_eigen(self, tensor):
        # feature scaling (standardize data)
        tensor_std = StandardScaler().fit_transform(tensor);
        # covariance matrix
        tensor_covar = np.cov(tensor.T)
        # eigen decomposition
        eig_values, eig_vectors = np.linalg.eig(tensor_covar)


    def uncompress(self, tensor):
        pass;
