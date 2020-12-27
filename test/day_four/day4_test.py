import src.day_four as validator
from test_data_day4 import get_test_data


def test_password_with_all_fields_is_valid():
    password = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm'''
    is_valid = validator.are_required_params_present(password)
    assert is_valid == True


def test_password_missing_required_field_is_invalid():
    password = '''iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929'''
    is_valid = validator.are_required_params_present(password)
    assert is_valid == False


def test_password_missing_two_fields_is_invalid():
    password = '''hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''
    is_valid = validator.are_required_params_present(password)
    assert is_valid == False


def test_password_missing_only_cid_is_valid():
    password = '''hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm'''
    is_valid = validator.are_required_params_present(password)
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


# byr
def test_byr_less_or_equal_2002_is_valid():
    is_valid = validator.validate_byr('2002')
    assert is_valid == True


def test_byr_greater_than_2002_is_invalid():
    is_valid = validator.validate_byr('2003')
    assert is_valid == False


def test_byr_less_than_1920_is_invalid():
    is_valid = validator.validate_byr('1919')
    assert is_valid == False


def test_byr_is_not_a_number_is_invalid():
    is_valid = validator.validate_byr('aaa')
    assert is_valid == False


# iyr

def test_iyr_less_or_equal_2020_is_valid():
    is_valid = validator.validate_iyr('2020')
    assert is_valid == True


def test_iyr_greater_than_2020_is_invalid():
    is_valid = validator.validate_iyr('2021')
    assert is_valid == False


def test_byr_less_than_2010_is_invalid():
    is_valid = validator.validate_iyr('2009')
    assert is_valid == False


def test_iyr_is_not_a_number_is_invalid():
    is_valid = validator.validate_iyr('aaa')
    assert is_valid == False


# eyr
def test_eyr_less_or_equal_2030_is_valid():
    is_valid = validator.validate_eyr('2030')
    assert is_valid == True


def test_eyr_greater_than_2030_is_invalid():
    is_valid = validator.validate_eyr('2031')
    assert is_valid == False


def test_eyr_less_than_2020_is_invalid():
    is_valid = validator.validate_eyr('2019')
    assert is_valid == False


def test_eyr_is_not_a_number_is_invalid():
    is_valid = validator.validate_eyr('aaa')
    assert is_valid == False


# hgt
def test_hgt_cm_greater_or_equals_to_150_is_valid():
    is_valid = validator.validate_hgt('150cm')
    assert is_valid == True


def test_hgt_cm_greater_than_193_is_invalid():
    is_valid = validator.validate_hgt('194cm')
    assert is_valid == False


def test_hgt_cm_less_than_150_is_invalid():
    is_valid = validator.validate_hgt('149cm')
    assert is_valid == False


def test_hgt_in_greater_or_equals_to_76_is_valid():
    is_valid = validator.validate_hgt('76in')
    assert is_valid == True


def test_hgt_cm_greater_than_76_is_invalid():
    is_valid = validator.validate_hgt('77in')
    assert is_valid == False


def test_hgt_cm_less_than_59_is_invalid():
    is_valid = validator.validate_hgt('58in')
    assert is_valid == False


def test_hgt_without_unit_is_invalid():
    is_valid = validator.validate_hgt('58')
    assert is_valid == False


def test_hgt_without_value_is_invalid():
    is_valid = validator.validate_hgt('cmd')
    assert is_valid == False


# hcl
def test_hcl_pound_six_chars_numbers_letters_is_valid():
    is_valid = validator.validate_hcl('#123abc')
    assert is_valid == True


def test_hcl_without_is_invalid():
    is_valid = validator.validate_hcl('123abc')
    assert is_valid == False


def test_hcl_without_required_number_of_chars_is_invalid():
    is_valid = validator.validate_hcl('#123ab')
    assert is_valid == False


# ecl

def test_ecl_with_value_amb_is_valid():
    is_valid = validator.validate_ecl('amb')
    assert is_valid == True


def test_with_other_value_is_invalid():
    is_valid = validator.validate_ecl('aaa')
    assert is_valid == False


def test_ecl_with_value_blu_is_valid():
    is_valid = validator.validate_ecl('blu')
    assert is_valid == True


#
def test_ecl_with_value_brn_is_valid():
    is_valid = validator.validate_ecl('brn')
    assert is_valid == True


def test_ecl_with_value_gry_is_valid():
    is_valid = validator.validate_ecl('gry')
    assert is_valid == True


def test_ecl_with_value_grn_is_valid():
    is_valid = validator.validate_ecl('grn')
    assert is_valid == True


def test_ecl_with_value_hzl_is_valid():
    is_valid = validator.validate_ecl('hzl')
    assert is_valid == True


def test_ecl_with_value_oth_is_valid():
    is_valid = validator.validate_ecl('oth')
    assert is_valid == True


# pid
def test_pid_with_leasing_zeros_and_numbers_from_1_to_9_is_valid():
    is_valid = validator.validate_pid('012345678')
    assert is_valid == True


def test_pid_with_all_zeros_is_valid():
    is_valid = validator.validate_pid('000000000')
    assert is_valid == True


def test_pid_without_required_length_is_invalid():
    is_valid = validator.validate_pid('01234567')
    assert is_valid == False


def test_pid_with_required_len_and_with_other_chars_is_invalid():
    is_valid = validator.validate_pid('01234567a')
    assert is_valid == False


def test_count_invalid_passwords_with_validations():
    passwords = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007'''
    num_of_valid_passwords = validator.report_valid_passwords_with_validations(passwords)
    assert num_of_valid_passwords == 0


def test_count_valid_passwords_with_validations():
    passwords = '''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''
    num_of_valid_passwords = validator.report_valid_passwords_with_validations(passwords)
    assert num_of_valid_passwords == 4


def test_report_valid_passwords_with_validations():
    num_of_valid_passwords = validator.report_valid_passwords_with_validations(get_test_data())
    assert num_of_valid_passwords == 111