from src.day_three import is_open_square, count_total_trees_in_slope
from test_data_day_3 import get_test_data


def test_square_is_open_if_world_map_contains_a_dot_in_coordinate():
    world_map = [".#.#....##.......#..........#.."]
    is_open = is_open_square(world_map, 0, 0)
    assert is_open == True


def test_square_has_a_three_if_world_map_contains_an_hashtag_in_coordinate():
    world_map = [".#.#....##.......#..........#.."]
    is_open = is_open_square(world_map, 0, 1)
    assert is_open == False


def test_square_duplicate_original_line_row_is_col_is_greater_than_line():
    world_map = [".#.#....##.......#..........#.."]
    is_open = is_open_square(world_map, 0, 41)
    assert is_open == True


def test_count_total_trees_with_small_map():
    world_map = create_small_map()
    total_trees = count_total_trees_in_slope(world_map, 3, 1)
    assert total_trees == 7


def create_small_map():
    world_map = ["..##.......",
                 "#...#...#..",
                 ".#....#..#.",
                 "..#.#...#.#",
                 ".#...##..#.",
                 "..#.##.....",
                 ".#.#.#....#",
                 ".#........#",
                 "#.##...#...",
                 "#...##....#",
                 ".#..#...#.#"]
    return world_map


def test_count_total_trees():
    world_map = get_test_data()
    total_trees = count_total_trees_in_slope(world_map, 3, 1)
    assert total_trees == 228


def test_slope_1_1_with_small_map():
    world_map = create_small_map()
    total_trees = count_total_trees_in_slope(world_map, 1, 1)
    assert total_trees == 2


def test_slope_5_1_with_small_map():
    world_map = create_small_map()
    total_trees = count_total_trees_in_slope(world_map, 5, 1)
    assert total_trees == 3


def test_slope_7_1_with_small_map():
    world_map = create_small_map()
    total_trees = count_total_trees_in_slope(world_map, 7, 1)
    assert total_trees == 4


def test_slope_1_2_with_small_map():
    world_map = create_small_map()
    total_trees = count_total_trees_in_slope(world_map, 1, 2)
    assert total_trees == 2


def test_slope_1_1():
    world_map = get_test_data()
    total_trees = count_total_trees_in_slope(world_map, 1, 1)
    assert total_trees == 84


def test_slope_5_1():
    world_map = get_test_data()
    total_trees = count_total_trees_in_slope(world_map, 5, 1)
    assert total_trees == 89


def test_slope_7_1():
    world_map = get_test_data()
    total_trees = count_total_trees_in_slope(world_map, 7, 1)
    assert total_trees == 100


def test_slope_1_2():
    world_map = get_test_data()
    total_trees = count_total_trees_in_slope(world_map, 1, 2)
    assert total_trees == 40
