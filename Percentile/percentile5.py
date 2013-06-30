""" A pecentile is the value below which a given percentage of observations
in a set of observations falls. There is no standard method for calculating
a percentile so we will use the simplest, the nearest rank.

The below function implements an extremely naive algorithm for finding a 
percentile value. It can be improved in several ways.

Consider what this function is actually doing. Optimized functions exist
both within python itself and numpy which can do much of the work faster.

Instead of doing the same amount of work faster can the algorithm be changed
so that less work is done?

Links:
https://en.wikipedia.org/wiki/Percentile"""

import numpy as np

def percentile(observations, percentile):
    """Returns a percentile value
    
    For simplicity assumes that all observations are unique
    and the list does not need to be preserved"""
    rank = int(round(0.5 + len(observations) * percentile / 100.))
    obs = np.array(observations)
    offset = 0
    while True:
        pivot = np.random.choice(obs, 1)
        below_pivot = len(obs[obs <= pivot])
        if offset + below_pivot == rank:
            return pivot[0]
        elif offset + below_pivot < rank:
            obs = obs[obs > pivot]
            offset = offset + below_pivot
        elif offset + below_pivot > rank:
            obs = obs[obs <= pivot]


if __name__ == '__main__':
    import percentile_test
    percentile_test.evaluate(percentile)
