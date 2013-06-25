import numpy as np
import time

def evaluate(func, timeout=30, start=0, end=8, step=10):
    start_time = time.time()
    correct = {100: {0:0.416281038004, 
                        1:0.43738803527, 
                        2:0.330392582878, 
                        3:0.382869824458, 
                        4:0.409799671639,},
            1000: {0:0.415952318264,
                        1:0.405575036385,
                        2:0.411863813743,
                        3:0.385030876367,
                        4:0.411834542327},}
    for i in range(start, end):
        observations = 100 * step ** i
        times = []
        for j in range(5):
            np.random.seed(j)
            actual = np.random.random(observations)
            prediction = np.random.random(observations)
            iter_start = time.time()
            result = func(actual, prediction)
            iter_end = time.time()
            try:
                expected = correct[observations][j]
            except:
                expected = None
            if (expected != None) and (np.abs(result - expected) > 10**-10):
                raise Exception('Unexpected result: ', result, expected)
            times.append(iter_end - iter_start)
            if time.time() > start_time + timeout:
                break
        print 'For %010d length took %f seconds (av. from %d repeats)' % \
                (observations, np.array(times).mean(), len(times))
        if time.time() > start_time + timeout:
            break



