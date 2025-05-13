# routing/grid.py
import numpy as np
from routing.utils import mm_to_cells, place_circle, is_outer_pad

GRID_RES_MM = 0.127
PAD_RADIUS_MM = 0.25
VIA_RADIUS_MM = 0.25
NUM_LAYERS = 3

def create_layers_and_pads(rows, cols):
    size_mm = (max(rows, cols) + 4) * 1.0  # pad + margin
    grid_size = mm_to_cells(size_mm)
    layers = [np.zeros((grid_size, grid_size), dtype=np.uint8) for _ in range(NUM_LAYERS)]
    pad_coords = []

    offset = (rows - 1) * 1.0 / 2
    for r in range(rows):
        for c in range(cols):
            x = c * 1.0 - offset
            y = r * 1.0 - offset
            pad_coords.append((r, c, x, y))
            for layer in layers:
                place_circle(layer, x, y, PAD_RADIUS_MM, mark=1)
    return layers, pad_coords, size_mm

def place_outer_pads(layer, pad_coords, rows, cols):
    for r, c, x, y in pad_coords:
        if is_outer_pad(r, c, rows, cols):
            place_circle(layer, x + 1.0, y, 0.05, mark=2)  # pretend trace

def place_inner_vias(layers, pad_coords, rows, cols):
    for r, c, x, y in pad_coords:
        if not is_outer_pad(r, c, rows, cols):
            via_x = x + 0.5
            via_y = y
            for layer in layers:
                place_circle(layer, via_x, via_y, VIA_RADIUS_MM, mark=3)
