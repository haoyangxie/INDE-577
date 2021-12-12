# Gradient Descent

## Introduction
Gradient descent is an optimization algorithm used to minimize some function by iteratively moving in the direction of steepest descent as defined by the negative of the gradient. In machine learning, we use gradient descent to update the parameters of our model. Parameters refer to coefficients in Linear Regression and weights in neural networks.
![Gradient Descent](https://i.imgur.com/xnPvEok.gif)

## Contents 
In this notebook, I use the gradient descent algorithm, by changing the learning rate and the number of iterations, to continuously reduce the value of the cost function, to find the most optimal linear equation.

## Dataset
There is no specific dataset in this case. I set function y = 3x + 4 and add some Gaussian noise to generate the data.

## Software Requirements
The following packages will be needed to run the code below: 

* Matplotlib [documentationra](https://matplotlib.org/)
* Numpy [documentation](https://numpy.org/doc/)
