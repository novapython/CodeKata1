import time


def evaluate(init_fn, func):
    duration = 0
    start_time = time.time()
    for i in xrange(100):
        grid = init_fn()
        for j in xrange(100):
            grid = func(grid)
    end_time = time.time()
    duration = end_time - start_time
    print 'Expected results obtained over %.5f seconds' % duration
