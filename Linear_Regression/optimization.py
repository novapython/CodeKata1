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
import linear_regression as lr

def optimize(dataset, actual, weights=None, max_iter=1000, step_size=0.1):
    if weights == None:
        weights = np.random.random(dataset.shape[1])
    for i in range(max_iter):
        difference=[i-j for i,j in zip(lr.predict(dataset, weights), actual)]
        weights_change = [0] * len(weights)
        for obs, diff in zip(dataset, difference):
            for i,j in enumerate(obs):
                weights_change[i] += j * diff
        weights = [w-(step_size/len(dataset))*wc for w,wc in \
                zip(weights,weights_change)]
    return weights

if __name__ == '__main__':
    import optimization_test
    optimization_test.evaluate(optimize)
