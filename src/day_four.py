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


def is_password_valid(password):
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
        if is_password_valid(password):
            num_of_valid_passwords += 1
    return num_of_valid_passwords
