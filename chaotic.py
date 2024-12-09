import numpy as np
import matplotlib.pyplot as plt

# Define random number generator
rng = np.random.default_rng()

# Generate random grid of floating point numbers [0,1]
grid = rng.random((50, 50))

print(grid)

# Visualize the grid
plt.imshow(grid, cmap="viridis")
plt.colorbar()
plt.title("Grid Visualization")
plt.show()
