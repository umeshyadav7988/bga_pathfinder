# routing/utils.py
import numpy as np
import matplotlib.pyplot as plt

GRID_RES_MM = 0.127
HUB_COORD = (5.0, 5.0)

def mm_to_cells(mm):
    return int(np.ceil(mm / GRID_RES_MM))

def coord_to_grid(x_mm, y_mm):
    return int(x_mm / GRID_RES_MM), int(y_mm / GRID_RES_MM)

def place_circle(grid, x_mm, y_mm, radius_mm, mark=1):
    cx, cy = coord_to_grid(x_mm, y_mm)
    r_cells = mm_to_cells(radius_mm)
    for dx in range(-r_cells, r_cells+1):
        for dy in range(-r_cells, r_cells+1):
            if dx**2 + dy**2 <= r_cells**2:
                gx, gy = cx + dx, cy + dy
                if 0 <= gx < grid.shape[1] and 0 <= gy < grid.shape[0]:
                    grid[gy, gx] = mark

def is_outer_pad(r, c, rows, cols):
    return r == 0 or r == rows - 1 or c == 0 or c == cols - 1

def plot_layer(layer, title="Layer"):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_title(title)
    ax.imshow(layer, cmap="nipy_spectral", origin="lower")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    return fig
