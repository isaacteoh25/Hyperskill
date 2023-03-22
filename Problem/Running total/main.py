new = [int(n) for n in input()]

tot = []
cum_sum = 0
for x in new:
    cum_sum += x
    tot.append(cum_sum)
print(tot)

num_list = [int(x) for x in input()]
print([sum(num_list[:x + 1]) for x in range(len(num_list))])