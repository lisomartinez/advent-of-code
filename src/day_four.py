import re

fields_key = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid'
}


def are_required_params_present(password):
    fields = re.split(r"[\s\n]", password)
    fields_present = 0
    is_cid_missing = 1
    for field in fields:
        key, value = tuple(field.split(':'))
        if key in fields_key:
            fields_present += 1
        if key == 'cid':
            is_cid_missing = 0
    return fields_present == len(fields_key) - is_cid_missing


def split_lines(passwords):
    return passwords.split('\n\n')


def report_valid_passwords(passwords):
    list_of_passwords = split_lines(passwords)
    num_of_valid_passwords = 0
    for password in list_of_passwords:
        if are_required_params_present(password):
            num_of_valid_passwords += 1
    return num_of_valid_passwords


def validate_byr(param):
    try:
        year = int(param)
        return True if 2002 >= year >= 1920 else False
    except ValueError:
        return False


def validate_iyr(param):
    try:
        year = int(param)
        return True if 2020 >= year >= 2010 else False
    except ValueError:
        return False


def validate_eyr(param):
    try:
        year = int(param)
        return True if 2030 >= year >= 2020 else False
    except ValueError:
        return False


def validate_hgt(param):
    has_valid_format = re.match('[0-9]*(cm$|in$)', param)
    if has_valid_format is None:
        return False

    unit = param[-2:]
    value = int(param[:-2])
    if unit == 'cm':
        return True if 193 >= value >= 150 else False
    elif unit == 'in':
        return True if 76 >= value >= 59 else False


def validate_hcl(param):
    has_length = len(param) == 7
    has_format = re.match('^#[0-9]*[a-z]*', param)
    return True if has_length and has_format is not None else False


def validate_ecl(param):
    values = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    return True if param in values else False


def validate_pid(param):
    has_required_len = len(param) == 9
    has_valid_format = re.match('^[0]{0,9}[0-9]{1,9}$', param)
    return True if has_required_len and has_valid_format is not None else False


validators = {'byr': validate_byr, 'iyr':  validate_iyr, 'eyr':  validate_eyr,
              'hgt':  validate_hgt, 'hcl':  validate_hcl, 'ecl':  validate_ecl,
              'pid':  validate_pid, 'cid':  lambda x: True}


def are_required_params_valid(password):
    fields = re.split(r"[\s\n]", password)
    fields_present = 0
    is_cid_missing = 1
    for field in fields:
        key, value = tuple(field.split(':'))
        if key in fields_key:
            validator = validators[key]
            is_valid = validator(value)
            if is_valid is True:
                fields_present += 1
        if key == 'cid':
            is_cid_missing = 0
    return fields_present == len(fields_key) - is_cid_missing


def report_valid_passwords_with_validations(passwords):
    list_of_passwords = split_lines(passwords)
    num_of_valid_passwords = 0
    for password in list_of_passwords:
        if are_required_params_valid(password):
            num_of_valid_passwords += 1
    return num_of_valid_passwords
