from typing import Set


def mid_of_range(lower_half, upper_half):
    return lower_half + (upper_half - lower_half) // 2


def find_half(command: str, lower_half: int, upper_half: int) -> (int, int):
    if command == 'F' or command == 'L':
        return lower_half, mid_of_range(lower_half, upper_half)
    elif command == 'B' or command == 'R':
        return mid_of_range(lower_half, upper_half) + 1, upper_half
    else:
        raise ValueError


def find_row(rows: str) -> int:
    lower_half = 0
    upper_half = 127
    for row in rows:
        lower_half, upper_half = find_half(row, lower_half, upper_half)
    return upper_half


def find_col(cols: str) -> int:
    lower_half = 0
    upper_half = 7
    for col in cols:
        lower_half, upper_half = find_half(col, lower_half, upper_half)
    return upper_half


def find_seat_id(commands: str) -> int:
    row = find_row(commands[0:7])
    col = find_col(commands[7:11])
    return (row * 8) + col


def find_max_seat_id(seats):
    max_id = 0
    for seat in seats:
        seat_id = find_seat_id(seat)
        if seat_id > max_id:
            max_id = seat_id
    return max_id


def find_misssing_seat_id(seats):
    seat_id_set: Set = set()
    min_id = -1
    max_id = 1
    for seat in seats:
        seat_id = find_seat_id(seat)
        seat_id_set.add(seat_id)
        min_id = set_min_id(min_id, seat_id)
        max_id = set_max_id(max_id, seat_id)
    return find_missing_in_expected_range(max_id, min_id, seat_id_set)


def find_missing_in_expected_range(max_id, min_id, seat_id_set):
    missing = 0
    for sid in range(min_id, max_id + 1):
        if sid not in seat_id_set:
            missing = sid
    return missing


def set_max_id(max_id, seat_id):
    if seat_id > 1 and seat_id > max_id:
        max_id = seat_id
    return max_id


def set_min_id(min_id, seat_id):
    if seat_id == -1 or seat_id < min_id:
        min_id = seat_id
    return min_id