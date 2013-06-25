import numpy as np
import time

import linear_regression
import RMSE

def evaluate(func, timeout=30, start=0, end=6, step=10):
    start_time = time.time()
    for i in range(start, end):
        observations = 100 * step ** i
        times = []
        for j in range(5):
            np.random.seed(j)
            dataset = np.random.random((observations, 3))
            actual = 10*dataset[:,0] + 5*dataset[:,1] + 2*dataset[:,2] + \
                    dataset[:,0] ** 2 + 2 * dataset[:,1] ** 2
            iter_start = time.time()
            start_weights = func(dataset, actual, max_iter=0)
            end_weights = func(dataset, actual, start_weights)
            iter_end = time.time()
            start_error = RMSE.rmse(actual, 
                    linear_regression.predict(dataset, start_weights))
            end_error = RMSE.rmse(actual,
                    linear_regression.predict(dataset, end_weights))
            if end_error > start_error:
                raise Exception('Error has increased %f -> %f' % \
                        (start_error, end_error))
            if end_error > 0.9:
                raise Exception('Error is unusually high %f' % end_error)
            times.append(iter_end - iter_start)
            if time.time() > start_time + timeout:
                break
        print 'For %010d observations took %f seconds (av. from %d repeats)'\
                % (observations, np.array(times).mean(), len(times))
        print 'Last set of weights were %s and error went from %f to %f' % \
                (str(end_weights), start_error, end_error)
        if time.time() > start_time + timeout:
            break



