# Linear Regression

## Introduction

Linear regression attempts to model the relationship between two variables by fitting a linear equation to observed data. One variable is considered to be an explanatory variable, and the other is considered to be a dependent variable. For example, a modeler might want to relate the weights of individuals to their heights using a linear regression model.
Before attempting to fit a linear model to observed data, a modeler should first determine whether or not there is a relationship between the variables of interest. This does not necessarily imply that one variable causes the other (for example, higher SAT scores do not cause higher college grades), but that there is some significant association between the two variables. A scatterplot can be a helpful tool in determining the strength of the relationship between two variables. If there appears to be no association between the proposed explanatory and dependent variables (i.e., the scatterplot does not indicate any increasing or decreasing trends), then fitting a linear regression model to the data probably will not provide a useful model. A valuable numerical measure of association between two variables is the correlation coefficient, which is a value between -1 and 1 indicating the strength of the association of the observed data for the two variables.

A linear regression line has an equation of the form Y = a + bX, where X is the explanatory variable and Y is the dependent variable. The slope of the line is b, and a is the intercept (the value of y when x = 0).

## Contents 
In this notebook, we first clean up the data and remove invalid data. Then remove some features that have nothing to do with housing prices, leaving only those that are related to housing prices. Then perform a simple linear regression, find out the characteristics that have the greatest relationship with house prices through heatmap, and perform linear regression with house prices one by one. Finally, we select ten characteristics that are most relevant to housing prices to perform multiple linear regression on housing prices.


## Dataset
This dataset contains house sale prices for King County, which includes Seattle. It includes homes sold between May 2014 and May 2015.  

The data contains such attributes as id, date, price, number of bedrooms, number of bathrooms, living area, lot area, floors, whether close to lake, view, condition, grade, basement area, built year, renovated year, zipcode, latitude, longitude.



## Software Requirements
The following packages will be needed to run the code below: 

* Pandas [documentation](https://pandas.pydata.org/docs/)
* Matplotlib [documentationra](https://matplotlib.org/)
* Numpy [documentation](https://numpy.org/doc/)
* Seaborn [documentation](https://seaborn.pydata.org/)


