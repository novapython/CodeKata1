"""
This solution uses the scipy.ndimage module.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.ioff() # make sure interactive mood is off

# This solution uses the scipy.ndimage module
from scipy import ndimage

# Make sure you read the docstring of ndimage.generic_filter.

from diffusion_model import init_grid, plot_grid
from naive_solution import spread

###################
# Expert Solution #
###################

def simulate_fire(grid_size, prob_tree, prob_burning, prob_lightning,
                  prob_immune, t):
    grids = []
    grid = init_grid(grid_size, prob_tree, prob_burning)
    grids.append(grid)
    for i in range(t):
        new_grid = np.zeros_like(grid)
        ndimage.generic_filter(grids[-1], spread, size=3, mode="constant",
                               output=new_grid,
                               # these are passed to spread
                               extra_arguments=(prob_immune,
                                                prob_lightning))
        grids.append(new_grid.copy())
    return grids


if __name__ == "__main__":
    grid_size = 50
    prob_tree = .8
    prob_burning = .0005
    prob_immune = .25
    prob_lightning = .00001

    # Optionally, set a *seed* to make the random numbers reproducible.

    np.random.seed(123)

    t = 50

    grids = simulate_fire(grid_size, prob_tree, prob_burning, prob_lightning,
                          prob_immune, t)

    for i, fire in enumerate(grids):
        fig = plot_grid(fire)
        fig.savefig("fire_animate%02d.png" % i)
    plt.close('all')

    # You will need to install ffmpeg to make the animation.
    # http://www.ffmpeg.org/
    import os
    os.system("ffmpeg -f image2 -r 2 -i fire_animate%02d.png -r 30 animated_fire2.webm")
