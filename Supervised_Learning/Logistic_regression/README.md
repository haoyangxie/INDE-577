# Logistic Regression

## Introduction
Logistic Regression is a machine learning method used to solve binary classification (0 or 1) problems, which is used to estimate the possibility of something. For example, the possibility of a user buying a certain product, the possibility of a certain patient suffering from a certain disease, and the possibility of a certain advertisement being clicked by the user, etc. Note that "possibility" is used here, not mathematical "probability". The result of logisitc regression is not a probability value in the mathematical definition and cannot be used directly as a probability value. The result is often used for weighted summation with other eigenvalues instead of direct multiplication.

Logistic Regression and Linear Regression are both a generalized linear model. Logistic regression assumes that the dependent variable y follows a Bernoulli distribution, while linear regression assumes that the dependent variable y follows a Gaussian distribution. Therefore, there are many similarities with linear regression. If the Sigmoid mapping function is removed, the logistic regression algorithm is a linear regression. It can be said that logistic regression is theoretically supported by linear regression, but logistic regression introduces non-linear factors through the Sigmoid function, so it can easily handle the 0/1 classification problem.

## Contents 
In this notebook, we will be using a User dataset, to predict if a user will purchased a particular product based on some attributes using logistic regression from scratch.

## Dataset
This is a dataset to determine whether a user purchased a particular product. There are five columns, such as user id, gender, age, estimated salary and whether these users will purchased a particular product. 



## Software Requirements
The following packages will be needed to run the code below: 

* Pandas [documentation](https://pandas.pydata.org/docs/)
* Matplotlib [documentationra](https://matplotlib.org/)
* Numpy [documentation](https://numpy.org/doc/)
* Scikit-learn [documentation](https://scikit-learn.org/stable/)


