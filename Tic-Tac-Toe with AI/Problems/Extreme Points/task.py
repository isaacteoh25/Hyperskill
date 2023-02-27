# The following line creates a dictionary from the input. Do not modify it, please
import json

test_dict = json.loads(input())
# test_dict = {"a": 43, "b": 1, "c": 456}
print('min:', min(test_dict, key = lambda k: test_dict[k]))
print('max:', max(test_dict, key = lambda k: test_dict[k]))
# Work with the 'test_dict'

# print("min:", min(test_dict, key=test_dict.get) + "\n" + "max:", max(test_dict, key=test_dict.get))

# print('min:', min(test_dict.items(), key=lambda x: x[1])[0])
# print('max:', max(test_dict.items(), key=lambda x: x[1])[0])

# td = [[k, v] for k, v in test_dict.items()]
# td.sort(key=lambda x: x[1])
# print("min: ", td[0][0], "\nmax: ", td[-1][0], sep="")

# mi = min(test_dict.values())
# ma = max(test_dict.values())
# for key, value in test_dict.items():
#     if value == mi:
#         minimal = key
#     elif value == ma:
#         maximal = key
#     else:
#         continue
# print("min:", minimal)
# print("max:", maximal)

# print("min:", ", ".join([x for x in test_dict.keys() if test_dict.get(x) == min(test_dict.values())]))
# print("max:", ", ".join([x for x in test_dict.keys() if test_dict.get(x) == max(test_dict.values())]))