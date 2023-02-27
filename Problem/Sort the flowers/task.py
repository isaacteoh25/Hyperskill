# the following line creates a list from the input, do not modify it, please
# prices = [float(price) for price in input().split()]
import re

prices = [0.75, 1.3, 1, 0.70 ]
# your code below
# print(prices.sort(reverse=True), key=float)
list1 = sorted(prices, key=float, reverse=True)
print(list1)

print (re.match('exclamation mark.', 'exclamation mark\n!'))