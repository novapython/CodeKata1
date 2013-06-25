import numpy as np
import matplotlib.pyplot as plt
plt.ioff() # make sure interactive mood is off

from diffusion_model import init_grid, plot_grid

##################
# Naive Solution #
##################

# Define the spread function

def spread(small_grid, prob_immune, prob_lightning):
    """
    small_grid is a flattened 3x3 array
    """
    # no tree or burned down
    if (small_grid[4] == 2 or small_grid[4] == 0):
        return 0
    # any neighbors are burning
    elif ((small_grid[1::2] == 2).any() and
         # it's burning now
         np.random.binomial(1, 1 - prob_immune)):
        return 2
    # it hasn't caught fire yet
    elif np.random.binomial(1, (1 - prob_immune)*prob_lightning):
        return 2
    else:
        return 1

# Pad the grid for boundary conditions. Add a row of zeros to the top and bottom and left and right.

def pad_grid(grid, grid_size):
    zeros = np.zeros(grid_size)
    padded_grid = np.column_stack((zeros, grid, zeros))
    zeros = np.zeros(grid_size + 2)
    padded_grid = np.row_stack((zeros, padded_grid, zeros))
    return padded_grid


if __name__ == "__main__":

    grid_size = 50
    prob_tree = .8
    prob_burning = .0005
    prob_immune = .25
    prob_lightning = .00001

    # Optionally, set a *seed* to make the random numbers reproducible.

    np.random.seed(123)

    grid = init_grid(grid_size, prob_tree, prob_burning)

    # Run the simulation

    t = 50
    grids = [grid.copy()]

    for i in range(t):
        padded_grid = pad_grid(grids[-1], grid_size)
        new_grid = np.zeros_like(grid)
        for j in range(1, grid_size + 1):
            for k in range(1, grid_size + 1):
                new_grid[j-1, k-1] = spread(padded_grid[j-1:j+2,
                                                        k-1:k+2].flatten(),
                                            prob_immune,
                                            prob_lightning)
        grids.append(new_grid.copy())

    # Save each figure so we can animate them.

    for i, fire in enumerate(grids):
        fig = plot_grid(fire)
        fig.savefig("fire_animate%02d.png" % i)
    plt.close('all')


    # You will need to install ffmpeg to make the animation.
    # http://www.ffmpeg.org/
    import os
    os.system("ffmpeg -f image2 -r 2 -i fire_animate%02d.png -r 30 animated_fire.webm")
