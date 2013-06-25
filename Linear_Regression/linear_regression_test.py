import hashlib
import numpy as np
import time

def evaluate(func, timeout=30, start=0, end=6, step=10):
    start_time = time.time()
    correct = {100: {0:'5af447016a97919f2a8ba944318f7fb945716f83',
                    1:'a290f255340e986f5f941c040aba211a476ae934',
                    2:'1d55ed5577423ef2b52c75f31991faecaaf4a054',
                    3:'a17e2007c0fd5942d163496a647775c96e3a4e40',
                    4:'95f2b5506e1a83a608cf8262525f8cdf121917b0'},}
    for i in range(start, end):
        observations = 100 * step ** i
        times = []
        for j in range(5):
            np.random.seed(j)
            weights = np.random.random(5)
            dataset = np.random.random((observations, 5))
            iter_start = time.time()
            result = func(dataset, weights)
            iter_end = time.time()
            try:
                expected = correct[observations][j]
                result = hashlib.sha1(str(list(result))).hexdigest()
            except:
                expected = None
            if (expected != None) and (result != expected):
                raise Exception('Unexpected result: ', result, expected)
            times.append(iter_end - iter_start)
            if time.time() > start_time + timeout:
                break
        print 'For %010d length took %f seconds (av. from %d repeats)' % \
                (observations, np.array(times).mean(), len(times))
        if time.time() > start_time + timeout:
            break



