# routing/utils.py
import numpy as np
import matplotlib.pyplot as plt

GRID_RES_MM = 0.127

def mm_to_cells(mm):
    return int(np.ceil(mm / GRID_RES_MM))

def coord_to_grid(x_mm, y_mm):
    return int(round(x_mm / GRID_RES_MM)), int(round(y_mm / GRID_RES_MM))

def grid_to_coord(x_cell, y_cell):
    return x_cell * GRID_RES_MM, y_cell * GRID_RES_MM

def place_circle(grid, x_mm, y_mm, radius_mm, mark=1):
    cx, cy = coord_to_grid(x_mm, y_mm)
    r_cells = mm_to_cells(radius_mm)
    for dx in range(-r_cells, r_cells + 1):
        for dy in range(-r_cells, r_cells + 1):
            if dx**2 + dy**2 <= r_cells**2:
                gx, gy = cx + dx, cy + dy
                if 0 <= gx < grid.shape[1] and 0 <= gy < grid.shape[0]:
                    grid[gy, gx] = mark

def is_outer_pad(r, c, rows, cols):
    return r == 0 or r == rows - 1 or c == 0 or c == cols - 1

def plot_layers_with_paths(layers, paths, link_colors, base_colors, titles):
    fig, axs = plt.subplots(1, len(layers), figsize=(18, 6))
    line_colors = ["blue", "red", "magenta"]
    dot_colors = ["green"] * 3

    for i, (layer, path, link_color, base_color, title) in enumerate(zip(layers, paths, link_colors, base_colors, titles)):
        ax = axs[i]
        ax.set_title(title, fontsize=12)
        ax.imshow(layer, cmap="Greys", origin="lower")

        if path:
            px, py = zip(*path)
            fx, fy = zip(*[grid_to_coord(x, y) for x, y in zip(px, py)])
            ax.plot(fx, fy, color=line_colors[i], linewidth=1.5)
            ax.scatter(fx, fy, color=dot_colors[i], s=6)

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel("")

        if i == 0:
            ax.set_ylabel("Routes", fontsize=12)
        else:
            ax.set_ylabel("")

    plt.tight_layout()
    plt.subplots_adjust(wspace=0.1)
    plt.show()
