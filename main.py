# main.py
import numpy as np
import matplotlib.pyplot as plt
from routing.pathfinder import a_star

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Place a 2x2 obstacle in the center
grid[4:6, 4:6] = 1

# Define start and goal
start = (0, 0)
goal = (9, 9)

# Run A*
path = a_star(grid, start, goal)

# Visualize the result
if path:
    for x, y in path:
        grid[y][x] = 2  # Mark path on grid

    # Visual plot
    plt.imshow(grid, cmap="viridis", origin="lower")
    plt.title("A* Pathfinding Demo")
    plt.colorbar(label="0=Free, 1=Obstacle, 2=Path")
    plt.show()
else:
    print("No path found.")
