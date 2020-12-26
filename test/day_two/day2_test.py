from src.day_two import parse_entry, is_password_valid_by_number_of_ocurrences, count_number_of_valid_password, \
    is_password_valid_by_position
from test_data_day_2 import get_test_data
import pytest


def test_parse_entry_return_values():
    entry = "1-3 a: abcde"
    min, max, character, password = parse_entry(entry)
    assert min == 1
    assert max == 3
    assert character == 'a'
    assert password == 'abcde'


def test_password_meeting_policy_is_valid_by_occurrences():
    validity = is_password_valid_by_number_of_ocurrences("1-3 a: abcde")
    assert validity == True


def test_password_not_meeting_policy_is_invalid_by_occurrences():
    validity = is_password_valid_by_number_of_ocurrences("1-3 b: cdefg")
    assert validity == False


def test_number_of_valid_password_is_equals_to_398():
    number_of_valid_passwords = count_number_of_valid_password(get_test_data(),
                                                               is_password_valid_by_number_of_ocurrences)
    assert number_of_valid_passwords == 398


def test_password_meeting_policy_is_valid_by_position():
    validity = is_password_valid_by_position("1-3 a: abcde")
    assert validity == True


def test_password_not_meeting_policy_is_invalid_by_position_two_matchings():
    validity = is_password_valid_by_position("2-9 c: ccccccccc")
    assert validity == False


def test_password_not_meeting_policy_is_invalid_by_position_no_matchings():
    validity = is_password_valid_by_position("1-3 b: cdefg")
    assert validity == False


def test_number_of_valid_password_by_position_is_equals_to_562():
    number_of_valid_passwords = count_number_of_valid_password(get_test_data(),
                                                               is_password_valid_by_position)
    assert number_of_valid_passwords == 562
