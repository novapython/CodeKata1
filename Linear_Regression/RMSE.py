""" The Root-Mean-Square Error (RMSE) is a frequently used measure of the 
difference between the predictions of a model and the observed values.

The function below implements this measure. How might this be improved with
numpy? 

Links:
https://en.wikipedia.org/wiki/RMSE
"""

def rmse(actual, prediction):
    differences = []
    for a, p in zip(actual, prediction):
        differences.append(a - p)
    squared_differences = [i ** 2 for i in differences]
    mean_difference = sum(squared_differences) / len(actual)
    return mean_difference ** 0.5


if __name__ == '__main__':
    import RMSE_test
    RMSE_test.evaluate(rmse)
