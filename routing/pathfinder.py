import heapq
import numpy as np
from routing.utils import mm_to_cells, place_circle, is_outer_pad

GRID_RES_MM = 0.127
PAD_RADIUS_MM = 0.25
VIA_RADIUS_MM = 0.25
NUM_LAYERS = 3
PITCH_MM = 1.0

def create_layers_and_pads(rows, cols):
    size_mm = (max(rows, cols) + 4) * PITCH_MM
    grid_size = mm_to_cells(size_mm)
    layers = [np.zeros((grid_size, grid_size), dtype=np.uint8) for _ in range(NUM_LAYERS)]
    pad_coords = []

    offset_x = (cols - 1) * PITCH_MM / 2
    offset_y = (rows - 1) * PITCH_MM / 2

    for r in range(rows):
        for c in range(cols):
            x = c * PITCH_MM - offset_x
            y = r * PITCH_MM - offset_y
            pad_coords.append((r, c, x, y))
            for layer in layers:
                place_circle(layer, x, y, PAD_RADIUS_MM, mark=1)

    return layers, pad_coords, size_mm

def place_outer_pads(layer, pad_coords, rows, cols):
    for r, c, x, y in pad_coords:
        if is_outer_pad(r, c, rows, cols):
            place_circle(layer, x, y + 1.0, 0.05, mark=2)

def place_inner_vias(layers, pad_coords, rows, cols):
    for r, c, x, y in pad_coords:
        if not is_outer_pad(r, c, rows, cols):
            via_x = x + 0.5
            via_y = y
            for layer in layers:
                place_circle(layer, via_x, via_y, VIA_RADIUS_MM, mark=3)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(node, grid):
    x, y = node
    neighbors = []
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < grid.shape[1] and 0 <= ny < grid.shape[0]:
            if grid[ny][nx] == 0:
                neighbors.append((nx, ny))
    return neighbors

def a_star(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current_cost, current = heapq.heappop(open_set)
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for neighbor in get_neighbors(current, grid):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                priority = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (priority, tentative_g, neighbor))
    return None
