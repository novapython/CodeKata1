""" Magicicadas are a periodic cicada that only emerges once every few years
it what is known as a "Brood". Virginia is in the region of several of these
Broods, mostly Brood II and Brood XIX. Fortunately BroodII only emerges every
17 years, and BroodXIX emerges every 13 years.

Over the next 600 years, which years will these horrible beasts join forces
and descend on our state simultaneously?

Links:
http://en.wikipedia.org/wiki/Periodical_cicadas
"""
import numpy as np

def naive():
    broodII_years = []
    broodXIX_years = []
    
    broodII_emergence = 2013
    broodXIX_emergence = 2011
        
    years = np.arange(2013,2013+600)
    years = years[(years % 17 == (broodII_emergence % 17)) & \
            (years % 13 == (broodXIX_emergence % 13))]
    return list(years)

if __name__ == '__main__':
    import magicicada_test
    magicicada_test.evaluate(naive)
