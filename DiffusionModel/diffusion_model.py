"""
This program simulates a forest fire.

Each 'cell' can take a value 0, 1, or 2 for empty cell, non-burning tree, and burning tree respectively.

1. Make a grid with initial states.
   1. There should 50 cells.
   2. The probability of having a tree, `prob_tree = .8`
   3. The probability of a cell having a burning tree, conditional on there being a tree is `prob_burning = .0005`
2. Plot the initial grid with matplotlib.
3. Run a simulation via iterations for `t = 50` times.
   1. At each step, apply a function, `spread`, to each cell.
   2. `spread` takes the value of each cell and its neighbors to the North, South, East, and West.
   3. It returns the value of the cell at the next iteration.
   4. The returned value depends on whether a neighboring cell contains a burning tree. Fire can spread with a probability, `1 - prob_immune = .75`.
   5. Additionally, the tree can be struck by lightning and catch fire with `prob_lightning = .00001`.
4. The last thing we need to know is what to do at the boundaries. We will use **absorbing boundary conditions**. That means that edges are insulated and can only be effect by inside neighboring cells.
"""

import numpy as np
import matplotlib.pyplot as plt
plt.ioff() # make sure we're not doing interactive plotting


# The grid initialization function

def init_grid(n, prob_tree, prob_burning):
    lattice = np.random.binomial(n=1, p=prob_tree, size=(n,n))
    lattice *= np.random.binomial(n=1, p=prob_burning, size=(n,n)) + 1
    return lattice

# Plot the initial grid with matplotlib

from matplotlib import colors

def plot_grid(grid, ax=None):
    color_map = colors.ListedColormap(["white", "gray", "red"])
    bounds = [0, 1, 2, 3]
    norm = colors.BoundaryNorm(bounds, color_map.N)

    if ax is None:
        fig, ax = plt.subplots(figsize=(8,8))

    ax.imshow(grid, interpolation='none', cmap=color_map, norm=norm)
    ax.grid(False)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    return fig

if __name__ == "__main__":

    # Initialize the grid

    np.random.seed(123)

    grid = init_grid(50, .8, .0005)

    # Plot the grid

    fig = plot_grid(grid);
    plt.show()
    plt.close('all')
