import numpy as np

class Perceptron():
    def __init__(self, n_features, bias = True):
        self.n_features = n_features
        self.bias = bias

        self.w = np.random.rand(self.n_features)
        if self.bias == True:
            self.b = np.random.randn()

    def feed_forward(self, x):
        if self.bias == True:
            z = self.w @ x + self.b
            if z > 0:
                return 1
            else: return -1
        
        else:
            z = self.w @ x
            if z > 0:
                return 1
            else:
                return -1