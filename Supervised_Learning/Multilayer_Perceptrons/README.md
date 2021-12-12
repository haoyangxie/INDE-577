# Multilayer Perceptron

## Introduction
A multilayer perceptron (MLP) is a class of feedforward artificial neural network (ANN). The term MLP is used ambiguously, sometimes loosely to mean any feedforward ANN, sometimes strictly to refer to networks composed of multiple layers of perceptrons (with threshold activation); see § Terminology. Multilayer perceptrons are sometimes colloquially referred to as "vanilla" neural networks, especially when they have a single hidden layer. 
An MLP consists of at least three layers of nodes: an input layer, a hidden layer and an output layer. Except for the input nodes, each node is a neuron that uses a nonlinear activation function. MLP utilizes a supervised learning technique called backpropagation for training. Its multiple layers and non-linear activation distinguish MLP from a linear perceptron. It can distinguish data that is not linearly separable. 

## Contents 
In this notebook, we use MLP algorithm to train model to classify images of handwritten digits from `0-9` in MNIST dataset.

## Dataset
Data here is from the [MNIST dataset](http://yann.lecun.com/exdb/mnist/) of `28x28` pixel images of handwritten digits from `0-9`, which has an important place in the history of machine learning.

## Software Requirements
The following packages will be needed to run the code below: 

* Pandas [documentation](https://pandas.pydata.org/docs/)
* Matplotlib [documentationra](https://matplotlib.org/)
* Numpy [documentation](https://numpy.org/doc/)
* Scikit-learn [documentation](https://scikit-learn.org/stable/)
