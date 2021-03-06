from math import ceil


def is_open_square(world_map, row, col):
    line_len = len(world_map[row]) - 1
    if col > line_len:
        lines_to_add = ceil(col / line_len)
        extended_row = world_map[row] * lines_to_add
        world_map[row] = extended_row
    return world_map[row][col] == '.'


def count_total_trees_in_slope(world_map, x, y) -> int:
    col = x
    row = y
    num_of_trees = 0
    while row < len(world_map):
        is_open = is_open_square(world_map, row, col)
        if is_open is False:
            num_of_trees += 1
        col = col + x
        row = row + y
    return num_of_trees
