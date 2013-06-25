""" Linear regression is one approach to model the relationship between one
or more input variables (often called independent or explanatory variables) 
and an output (often called a dependent variable). 

Once the model is established predictions can be made about the dependent 
variable given a set of independent variables. As an example, the area of 
a house, the number of bathrooms, and the number of bedrooms could be used
to predict a sale price.

Linear regression can also be used to quantify the strength of the 
relationship between an independent variable and the dependent variable given
a dataset. As an example, how much value does an extra bathroom create?

The model consists of a weight given to each of the independent variables.

The below function returns a set of predictions given a dataset and a set
of weights. How can this be improved using numpy?

Links:
https://en.wikipedia.org/wiki/Linear_regression
"""
import numpy as np

def predict(observations, weights):
    return np.dot(observations, weights)

if __name__ == '__main__':
    import linear_regression_test
    linear_regression_test.evaluate(predict)
