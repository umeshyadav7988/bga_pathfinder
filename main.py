# main.py
import numpy as np
from routing.pathfinder import create_layers_and_pads, place_outer_pads, place_inner_vias, a_star
from routing.utils import plot_layers_with_paths, coord_to_grid

# Setup grid size
rows, cols = 6, 6
layers, pad_coords, size_mm = create_layers_and_pads(rows, cols)

# Place pads and vias
place_outer_pads(layers[0], pad_coords, rows, cols)
place_inner_vias(layers, pad_coords, rows, cols)

# Define hub coordinate in mm and convert to grid index
hub_coord_mm = (8.0, 8.0)
hub_idx = coord_to_grid(*hub_coord_mm)

# Mark the hub via location across all layers
for layer in layers:
    layer[hub_idx[1], hub_idx[0]] = 0  # ensure it's routable

# Setup paths
paths_per_layer = [[] for _ in range(len(layers))]

# --- Layer 0: Route a single outer pad to the hub ---
for r, c, x_mm, y_mm in pad_coords:
    if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
        start_idx = coord_to_grid(x_mm, y_mm + 1.0)
        layers[0][start_idx[1], start_idx[0]] = 0
        path = a_star(layers[0], start_idx, hub_idx)
        if path:
            for x, y in path:
                layers[0][y, x] = 4  # mark path
            paths_per_layer[0].append(path)
            break  # use only one trace to hub

# --- Layer 1: Extend a second ring pad to the hub ---
for r, c, x_mm, y_mm in pad_coords:
    if 1 <= r <= rows - 2 and 1 <= c <= cols - 2:
        start_idx = coord_to_grid(x_mm + 0.5, y_mm)  # dogbone via
        layers[1][start_idx[1], start_idx[0]] = 0
        path = a_star(layers[1], start_idx, hub_idx)
        if path:
            for x, y in path:
                layers[1][y, x] = 4  # mark path
            paths_per_layer[1].append(path)
            break

# --- Layer 2: Extend a deeper inner ring pad to the hub ---
for r, c, x_mm, y_mm in pad_coords:
    if 2 <= r <= rows - 3 and 2 <= c <= cols - 3:
        start_idx = coord_to_grid(x_mm + 0.5, y_mm)  # deeper dogbone
        layers[2][start_idx[1], start_idx[0]] = 0
        path = a_star(layers[2], start_idx, hub_idx)
        if path:
            for x, y in path:
                layers[2][y, x] = 4  # mark path
            paths_per_layer[2].append(path)
            break

# Visualize results
plot_layers_with_paths(
    layers,
    paths_per_layer,
    link_colors=["cyan", "red", "lime"],
    base_colors=["blue", "orange", "magenta"],
    titles=["Layer 1 (Top)", "Layer 2", "Layer 3"]
)