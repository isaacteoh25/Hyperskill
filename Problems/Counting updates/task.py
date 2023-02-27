def selection_sort(elements):
    updates = 0
    for i in range(len(elements) - 1):
        index = i

        for j in range(i + 1, len(elements)):
            if elements[j] < elements[index]:
                index = j
                updates += 1

        elements[i], elements[index] = elements[index], elements[i]
    return updates


n = int(input())
my_dict = dict()
for i in range(n):
    my_dict[i] = list(map(int, input().split(" ")))
index = 0
max_updates = 0
for i in range(n):
    upd_cnt = selection_sort(my_dict[i])
    if max_updates < upd_cnt:
        max_updates = upd_cnt
        index = i
print(str(index) + " " + str(max_updates))


# n = int(input())
#
# list_lists = []
# for _i in range(n):
#     list_lists.append([int(num) for num in input().split()])
#
# counter_counter = []
# for lst in list_lists:
#     counter_counter.append(selection_sort(lst))
#
# print(counter_counter.index(max(counter_counter)), max(counter_counter))