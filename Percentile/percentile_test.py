import numpy as np
import random
import time

def evaluate(func, timeout=30, start=0, end=8, step=10):
    start_time = time.time()
    for i in range(start, end):
        observations = 100 * step ** i
        expected = observations / 2
        times = []
        for j in range(5):
            sample = range(observations)
            random.shuffle(sample)
            iter_start = time.time()
            result = func(sample, 50)
            iter_end = time.time()
            if np.abs(result - expected) > 1:
                raise Exception('Unexpected result: ', result, expected)
            times.append(iter_end - iter_start)
            if time.time() > start_time + timeout:
                break
        print 'For %010d length took %f seconds (av. from %d repeats)' % \
                (observations, np.array(times).mean(), len(times))
        if time.time() > start_time + timeout:
            break



