import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets 

from single_neuron import Perceptron

df = datasets.load_iris(as_frame = True)
data = df['frame']
X = data[["sepal length (cm)", "sepal width (cm)"]].iloc[:100].to_numpy()
Y = data["target"].iloc[:100].to_numpy()

net = Perceptron(2)

print(net.feed_forward(X[0]))