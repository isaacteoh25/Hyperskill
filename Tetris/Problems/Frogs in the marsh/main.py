def number_of_frogs(year):
    if year == 1:
        return 120
    else:
        return 2 * (number_of_frogs(year - 1) - 50)


vowels = {'a', 'e', 'i', 'o', 'u'}


def find_apostrophe(word, start):
    i = word.index("'", start)

    if i == -1:
        print("1")
        return -1

    if i == 0:
        print("2")
        return find_apostrophe(word, 1)

    elif i == len(word) - 1:
        print("3")
        return -1

    else:
        previous_char = word[i - 1]
        if previous_char in set(vowels):
            print("4")
            return i

        else:
            print("5")
            return find_apostrophe(word, i + 1)

correct_index = find_apostrophe("'w'ord'", 0)

def power(base, exponent):
    # Any number to the zero power is 1
    if exponent == 0:
        return 1
    # Base case
    elif exponent == 1:
        return base
    # Recursive case
    else:
        return base * power(base, exponent - 1)

print(power(3,5))