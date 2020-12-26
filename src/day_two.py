def parse_entry(entry: str):
    fields = entry.split(' ')
    numbers_of_occurrences = fields[0]
    occurrences = numbers_of_occurrences.split('-')
    min: int = int(occurrences[0])
    max: int = int(occurrences[1])
    character = fields[1][0]
    password = fields[2]
    return min, max, character, password


def is_password_valid_by_number_of_ocurrences(entry) -> bool:
    minc, maxc, character, password = parse_entry(entry)
    number_ocurrences_found = password.count(character)
    return minc <= number_ocurrences_found <= maxc


def is_password_valid_by_position(entry) -> bool:
    first, second, character, password = parse_entry(entry)
    if len(password) < second:
        return False
    if password[first - 1] == character and password[second - 1] == character:
        return False
    if password[first - 1] == character or password[second - 1] == character:
        return True
    return False


def count_number_of_valid_password(entries, fn) -> int:
    number_of_valid_passwords = 0
    for entry in entries:
        is_valid = fn(entry)
        if is_valid is True:
            number_of_valid_passwords += 1
    return number_of_valid_passwords
