# K-Means clustering

## Introduction
K-means clustering is a type of unsupervised learning, which is used with unlabeled dataset. The goal of this algorithm is to find K groups in the data. The algorithm works iteratively to assign each data point to one of K groups based on the features that are provided. Data points are clustered based on feature similarity. The results of the K-means clustering algorithm are:

The centroids of the K clusters, which can be used to label new data
Labels for the training data (each data point is assigned to a single cluster)
K-means works by defining spherical clusters that are separable in a way so that the mean value converges towards the cluster center. Because of this, K-Means may underperform sometimes.

## Contents 
In this notebook, we use k-means clustering algorithm to classify all customers in the shopping mall based on the gender, age, annual income, and consumption level of them.


## Dataset
This data set has five columns, which are customer id, gender, age, annual income, and consumption level.

## Software Requirements
The following packages will be needed to run the code below: 

* Pandas [documentation](https://pandas.pydata.org/docs/)
* Matplotlib [documentationra](https://matplotlib.org/)
* Numpy [documentation](https://numpy.org/doc/)
* Seaborn [documentation](https://seaborn.pydata.org/)

