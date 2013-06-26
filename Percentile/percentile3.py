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
    obs = np.array(observations)
    rank = int(round(0.5 + len(observations) * percentile / 100.))
    return np.percentile(obs, percentile)
    ordered_observations = np.sort(obs)
    return ordered_observations[rank - 1]

if __name__ == '__main__':
    import percentile_test
    percentile_test.evaluate(percentile)

