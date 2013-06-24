""" The test script evaluates the passed function and tests for
the expected result. You should import this module, and call the
evalute() function from your solution code.
"""
import time


def evaluate(func):
    expected = 250166416500L
    start_time = time.time()
    for i in xrange(100):
        result = func()
        if result != expected:
            raise Exception('Unexpected result: ', result, expected)
    end_time = time.time()
    duration = end_time - start_time
    print 'Expected results obtained over %.5f seconds' % duration
