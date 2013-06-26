""" In the previous example we used a linear regression model to generate
predictions. By multiplying independent variables by weights we could
generate a predicted value for a dependent variable.

In this example we will generate an optimal set of weights. There are a
variety of different methods to do this. One of the simplest approaches is
gradient descent. This approach uses the error of the model to predict the 
direction the current weights must move in to be closer to the optimal
weights. The weights are then moved a small step in that direction and the
process repeats."""

import numpy as np
import linear_regression3 as lr

def optimize(dataset, actual, weights=None, max_iter=10000, step_size=0.1):
    if weights == None:
        weights = np.random.random(dataset.shape[1])
    for i in range(max_iter):
        #w = w - 0.0005 * np.dot(x.T, np.dot(x,w) - y)
        weights = weights - (step_size / dataset.shape[0]) * \
                np.dot(dataset.T, lr.predict(dataset, weights) - actual)
    return weights

if __name__ == '__main__':
    import optimization_test
    optimization_test.evaluate(optimize, start=0, end=4)
