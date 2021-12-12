# Decision Trees

## Introduction
A decision tree is a flowchart-like structure in which each internal node represents a "test" on an attribute (e.g. whether a coin flip comes up heads or tails), each branch represents the outcome of the test, and each leaf node represents a class label (decision taken after computing all attributes). The paths from root to leaf represent classification rules.
In decision analysis, a decision tree and the closely related influence diagram are used as a visual and analytical decision support tool, where the expected values (or expected utility) of competing alternatives are calculated.
A decision tree consists of three types of nodes: 
1.	Decision nodes – typically represented by squares
2.	Chance nodes – typically represented by circles
3.	End nodes – typically represented by triangles

## Contents 
In this notebook, I use decision tree model to analyse passenger data (ie name, age, gender, socio-economic class, etc) to predict whether passenger can survive.

## Dataset
The dataset called Titanic is from [kaggle](https://www.kaggle.com/c/titanic/data). The data has been split into two groups: training set (train.csv), test set (test.csv).
Dataset also includes gender_submission.csv, a set of predictions that assume all and only female passengers survive.

## Software Requirements
The following packages will be needed to run the code below: 

* Pandas [documentation](https://pandas.pydata.org/docs/)
* Matplotlib [documentationra](https://matplotlib.org/)
* Numpy [documentation](https://numpy.org/doc/)
* Scikit-learn [documentation](https://scikit-learn.org/stable/)
* Seaborn [documentation](https://seaborn.pydata.org/)
