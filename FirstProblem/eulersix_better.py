""" This solution uses numpy to apply (x ** 2) to each
element in the array, instead of iteration over a range
of numbers
"""
import numpy as np


def better():
    x = np.arange(1001, dtype='int64')
    sumsq = np.sum(x ** 2)
    sqsum = x.sum() ** 2

    return sqsum - sumsq

if __name__ == '__main__':
    import eulersix_test
    eulersix_test.evaluate(better)
