""" This test script expects a list containing the years which both
Magicicada Broods will attempt to destroy us all. This evaluation
will sort the list, so that shouldn't be your concern
"""
import time


def evaluate(func):
    expected = [2115, 2336, 2557]
    start_time = time.time()
    for i in xrange(100):
        result = sorted(func())
        if result != expected:
            raise Exception('Unexpected result: ', result, expected)
    end_time = time.time()
    duration = end_time - start_time
    print 'Expected results obtained over %.5f seconds' % duration
