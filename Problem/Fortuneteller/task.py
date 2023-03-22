# put your code here
number = int(input())
# print(sum(map(int, number)))
#
# sum_of_digits = 0
# for digit in str(number):
#   sum_of_digits += int(digit)
#
# print(sum_of_digits)
print(eval('+'.join(str(x) for x in input())))
generator = (int(n) for n in number)

print(sum(generator))