#!/usr/bin/python3


def roman_to_int(roman_string):
    count_sum = 0
    for n in range(0, len(roman_string)):
        numeral = roman_string[n]
        if numeral == "I":
            if n + 1 < len(roman_string) and roman_string[n + 1] != "I":
                count_sum -= 1
            else:
                count_sum += 1
        elif numeral == "V":
            count_sum += 5
        elif numeral == "X":
            count_sum += 10
        elif numeral == "L":
            count_sum += 50
        elif numeral == "C":
            count_sum += 100
        elif numeral == "D":
            count_sum += 500
    return count_sum
