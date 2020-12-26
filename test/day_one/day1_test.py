from test_data import get_test_data_as_set
from src.day_one import two_numbers_summing_2020, three_numbers_summing_2020
import pytest


def test_two_numbers_summing_2020():
    (n1, n2, total) = two_numbers_summing_2020(get_test_data_as_set())
    assert n1 == 1611
    assert n2 == 409
    assert total == 1611 * 409


def test_three_numers_summing_2020():
    (n1, n2, n3, total) = three_numbers_summing_2020(get_test_data_as_set())
    assert n1 == 250
    assert n2 == 1285
    assert n3 == 485
    assert total == 250 * 1285 * 485
