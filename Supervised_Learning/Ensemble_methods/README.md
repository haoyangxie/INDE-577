# Ensemble Learning

## Introduction
In statistics and machine learning, ensemble methods use multiple learning algorithms to obtain better predictive performance than could be obtained from any of the constituent learning algorithms alone. Unlike a statistical ensemble in statistical mechanics, which is usually infinite, a machine learning ensemble consists of only a concrete finite set of alternative models, but typically allows for much more flexible structure to exist among those alternatives.

## Contents 
In this notebook, I use knn, gradient descent, logistic regression, perceptron, support vector machines, decision tree, random forest to build models to predict the Titanic disaster to compare the scores of different methods. The result is as follow:  
![image](https://obohe.com/i/2021/12/13/8wnhgr.jpg)

## Dataset
The dataset called Titanic is from [kaggle](https://www.kaggle.com/c/titanic/data). The data has been split into two groups: training set (train.csv), test set (test.csv). The dataset contains few columns such as, whether passengers can survive, ticket class, sex, age in years, ticket number, passenger fare, cabin number.
Dataset also includes gender_submission.csv, a set of predictions that assume all and only female passengers survive.

## Software Requirements
The following packages will be needed to run the code below: 

* Pandas [documentation](https://pandas.pydata.org/docs/)
* Matplotlib [documentationra](https://matplotlib.org/)
* Numpy [documentation](https://numpy.org/doc/)
* Scikit-learn [documentation](https://scikit-learn.org/stable/)
* Seaborn [documentation](https://seaborn.pydata.org/)
* Tensorflow [documentation](https://www.tensorflow.org/)
