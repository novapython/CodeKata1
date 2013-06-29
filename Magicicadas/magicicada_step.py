""" Magicicadas are a periodic cicada that only emerges once every few years
it what is known as a "Brood". Virginia is in the region of several of these
Broods, mostly Brood II and Brood XIX. Fortunately BroodII only emerges every
17 years, and BroodXIX emerges every 13 years.

Over the next 600 years, which years will these horrible beasts join forces
and descend on our state simultaneously?

Links:
http://en.wikipedia.org/wiki/Periodical_cicadas
"""

def naive():
    broodII_years = []
    broodXIX_years = []
    
    broodII_emergence = 2013
    broodXIX_emergence = 2011
    
    broodII_years = range(broodII_emergence, broodII_emergence+600, 17)
    broodXIX_years = range(broodXIX_emergence, broodXIX_emergence+600, 13)    

    return set(broodII_years) & set(broodXIX_years)


if __name__ == '__main__':
    import magicicada_test
    magicicada_test.evaluate(naive)
