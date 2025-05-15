import numpy as np
from routing.pathfinder import create_layers_and_pads, place_outer_pads, place_inner_vias, a_star
from routing.utils import plot_layers_with_paths, coord_to_grid

# Setup grid size
rows, cols = 6, 6
layers, pad_coords, size_mm = create_layers_and_pads(rows, cols)

# Place pads and vias
place_outer_pads(layers[0], pad_coords, rows, cols)
place_inner_vias(layers, pad_coords, rows, cols)

# Routing parameters
hub_coord_mm = (8.0, 8.0)
hub_idx = coord_to_grid(*hub_coord_mm)
paths_per_layer = [[] for _ in range(len(layers))]

# Route from all outer pads to hub on Layer 0
for r, c, x_mm, y_mm in pad_coords:
    if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
        start_idx = coord_to_grid(x_mm, y_mm + 1.0)
        # Mark start and goal as free (0)
        layers[0][start_idx[1], start_idx[0]] = 0
        layers[0][hub_idx[1], hub_idx[0]] = 0
        path = a_star(layers[0], start_idx, hub_idx)
        if path:
            for x, y in path:
                layers[0][y, x] = 4  # mark path on layer
            paths_per_layer[0].append(path)

# Visualize results
plot_layers_with_paths(
    layers,
    paths_per_layer,
    link_colors=["cyan", "orange", "lime"],
    base_colors=["blue", "red", "magenta"],
    titles=["Layer 1 (Top)", "Layer 3", "Layer 4"]
)
