import numpy as np
import matplotlib.pyplot as plt


# Generate a grid of almost uniform numbers. We need a minute variation to represent the near uniform state of the early universe. 
grid = np.ones((50, 50))

print(grid)

# Visualize the grid
plt.imshow(grid, cmap="viridis")
plt.colorbar()
plt.title("Grid Visualization")
plt.show()

