def luhn(no):
    c = 0
    summ = 0
    second = False
    length = len(no);
    for i in range(length - 1, -1, -1):
        c = int(no[i])
        if second == True:
            c = c * 2
        summ = summ + c / 10
        summ = summ + c % 10
        second = not second
    if summ % 10 == 0:
        return True
    return False
print(luhn('4000009361788836'))

def is_passed_luhn_algorithm(number):
    luhn = [int(char) for char in str(number)]
    for i, num in enumerate(luhn):
        if (i + 1) % 2 == 0:
            continue
        temp = num * 2
        luhn[i] = temp if temp < 10 else temp - 9
    return sum(luhn) % 10 == 0

print(is_passed_luhn_algorithm('4000009361788836'))