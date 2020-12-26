def two_numbers_summing_2020(numbers):
    n1 = 0
    n2 = 0
    for number in numbers:
        dif = 2020 - number
        found = dif in numbers
        if found is True:
            print(f'found {number} + {dif} = 2020')
            n1 = number
            n2 = dif
            break
    answer = n1 * n2
    return n1, n2, answer


def three_numbers_summing_2020(numbers):
    n1 = 0
    n2 = 0
    n3 = 0
    list_of_numbers = list(numbers)
    for index, first_number in enumerate(list_of_numbers):
        for second_number_index in range(index + 1, len(list_of_numbers)):
            second_number = list_of_numbers[second_number_index]
            partial = first_number + second_number
            dif = 2020 - partial
            found = dif in numbers
            if found is True:
                n1 = first_number
                n2 = second_number
                n3 = dif
                return n1, n2, n3, n1 * n2 * n3
    return 0, 0, 0, 0
