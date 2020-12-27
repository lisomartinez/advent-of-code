import src.day_four as validator
from test_data_day4 import get_test_data


def test_password_with_all_fields_is_valid():
    password = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm'''
    is_valid = validator.is_password_valid(password)
    assert is_valid == True


def test_password_missing_required_field_is_invalid():
    password = '''iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929'''
    is_valid = validator.is_password_valid(password)
    assert is_valid == False


def test_password_missing_two_fields_is_invalid():
    password = '''hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''
    is_valid = validator.is_password_valid(password)
    assert is_valid == False


def test_password_missing_only_cid_is_valid():
    password = '''hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm'''
    is_valid = validator.is_password_valid(password)
    assert is_valid == True


def test_password_are_split_by_blanklines():
    passwords = create_short_list_of_passwords()
    lines = validator.split_lines(passwords)
    assert len(lines) == 4


def create_short_list_of_passwords():
    passwords = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''
    return passwords


def test_report_valid_passwords_short_list():
    passwords = create_short_list_of_passwords()
    valid_passwords = validator.report_valid_passwords(passwords)
    assert valid_passwords == 2


def test_report_valid_passwords():
    passwords = get_test_data()
    valid_passwords = validator.report_valid_passwords(passwords)
    assert valid_passwords == 233
