# the list with classes; please, do not modify it


fruits = ['apple', 'kiwi', 'banana','orange', 'apricot']

fruits_dict = {element: len(element) for element in fruits if len(element) > 5}
print(fruits_dict)
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
di = dict.fromkeys(groups, None)
di.update({groups[i]: int(input()) for i in range(int(input()))})
print(di)

import itertools

# your code here
h = []
k = int(input())
while k > 0:
    h.append(int(input()))
    k -= 1

p = dict(itertools.zip_longest(groups, h))
print(p)