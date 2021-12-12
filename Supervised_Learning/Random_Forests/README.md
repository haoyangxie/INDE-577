# Random Forest

## Introduction
Random forests or random decision forests are an ensemble learning method for classification, regression and other tasks that operates by constructing a multitude of decision trees at training time. For classification tasks, the output of the random forest is the class selected by most trees. For regression tasks, the mean or average prediction of the individual trees is returned. Random decision forests correct for decision trees' habit of overfitting to their training set. Random forests generally outperform decision trees, but their accuracy is lower than gradient boosted trees. However, data characteristics can affect their performance. 

## Contents 
In this notebook, I use random forest model to find the importance of different variables. To determine which characteristics are most relevant to the survival of passengers.

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

