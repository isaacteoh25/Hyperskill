from collections import Counter

text_list = input().split()
freq_counter = Counter(text_list)
 
# for word in text_list:
#     freq_defaultdict[word] += 1
 
a = freq_counter.most_common(1)
print(a[0][0])

# import statistics
# x = input().split()
# print(statistics.mode(x))

# input_string = input()
# input_list = [s for s in input_string.split(' ')]
# from collections import Counter
# freq_counter = Counter(input_list)
# mode = freq_counter.most_common(1)[0][0]
# print(mode)

# print(Counter(input().split()).most_common(1)[0][0])

# freq = {}
# for i in input().split():
#     freq[i] = freq.setdefault(i, 0) + 1
# print(max(freq, key=freq.get))

from collections import Counter, defaultdict
numbers = input().split()

# Mode with dict.setdefault
n_dict = dict()
for num in numbers:
    n_dict.setdefault(num, 0)
    n_dict[num] += 1
most_common_setdefault = sorted(n_dict, key=n_dict.get, reverse=True)[0]

# Mode with collections.defaultdict
n_defaultdict = defaultdict(int)
for num in numbers:
    n_defaultdict[num] += 1
most_common_defaultdict = sorted(n_defaultdict, key=n_defaultdict.get, reverse=True)[0]

# Mode with collections.Counter
n_counter = Counter(numbers)
most_common_counter = n_counter.most_common(1)[0][0]

result = None
if most_common_setdefault == most_common_defaultdict == most_common_counter:
    result = most_common_setdefault

print(result)