import pytest

import src.day_five as seat_finder
from test_data_day5 import get_test_data


def test_find_row_forward_half():
    min_row: int = 0
    max_row: int = 127
    res: (int, int) = seat_finder.find_half(command='F', lower_half=min_row, upper_half=max_row)
    assert res[0] == 0 and res[1] == 63


def test_find_row_back_half():
    min_row: int = 0
    max_row: int = 127
    res: (int, int) = seat_finder.find_half(command='B', lower_half=min_row, upper_half=max_row)
    assert res[0] == 64 and res[1] == 127


def test2():
    min_row: int = 32
    max_row: int = 63
    res: (int, int) = seat_finder.find_half(command='F', lower_half=min_row, upper_half=max_row)
    assert res[0] == 32 and res[1] == 47


def test3():
    min_row: int = 32
    max_row: int = 47
    res: (int, int) = seat_finder.find_half(command='B', lower_half=min_row, upper_half=max_row)
    assert res[0] == 40 and res[1] == 47


def test_find_row_raise_if_value_is_not_forward_or_back():
    with pytest.raises(ValueError):
        seat_finder.find_half(command='Z', lower_half=0, upper_half=127)


def test_find_rows():
    rows = 'FBFBBFF'
    row = seat_finder.find_row(rows)
    assert row == 44


def test_find_col_backward_half():
    min_row: int = 0
    max_row: int = 7
    res: (int, int) = seat_finder.find_half(command='R', lower_half=min_row, upper_half=max_row)
    assert res[0] == 4 and res[1] == 7


def test_find_col_forward_half():
    min_row: int = 4
    max_row: int = 7
    res: (int, int) = seat_finder.find_half(command='L', lower_half=min_row, upper_half=max_row)
    assert res[0] == 4 and res[1] == 5


def test_find_rows2():
    rows = 'BFFFBBF'
    row = seat_finder.find_row(rows)
    assert row == 70


def test_find_rows3():
    rows = 'FFFBBBF'
    row = seat_finder.find_row(rows)
    assert row == 14


def test_find_rows4():
    rows = 'BBFFBBF'
    row = seat_finder.find_row(rows)
    assert row == 102


def test_find_cols():
    cols = 'RLR'
    col = seat_finder.find_col(cols)
    assert col == 5


def test_find_cols2():
    cols = 'RRR'
    col = seat_finder.find_col(cols)
    assert col == 7


def test_find_cols3():
    cols = 'RLL'
    col = seat_finder.find_col(cols)
    assert col == 4


def test_find_seat_id():
    seat_code = 'FBFBBFFRLR'
    id = seat_finder.find_seat_id(seat_code)
    assert id == 357


def test_find_seat_id2():
    seat_code = 'BFFFBBFRRR'
    id = seat_finder.find_seat_id(seat_code)
    assert id == 567


def test_find_seat_id3():
    seat_code = 'FFFBBBFRRR'
    id = seat_finder.find_seat_id(seat_code)
    assert id == 119


def test_find_seat_id4():
    seat_code = 'BBFFBBFRLL'
    id = seat_finder.find_seat_id(seat_code)
    assert id == 820


def test_find_max():
    seats = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
    max_id = seat_finder.find_max_seat_id(seats)
    assert max_id == 820


def test_find_max_seat_id_from_test_data():
    seats = get_test_data()
    max_id = seat_finder.find_max_seat_id(seats)
    assert max_id == 922

def test_list_of_seats_id():
    seats = get_test_data()
    missing_seat_id = seat_finder.find_misssing_seat_id(seats)
    assert missing_seat_id == 747