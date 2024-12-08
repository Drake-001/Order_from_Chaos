import numpy as np

# Define random number generator
rng = np.random.default_rng()

# Generate random grid of floating point numbers [0,1]
grid = rng.random((50, 50))

print(grid)