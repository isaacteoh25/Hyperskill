def list_sum(some_list):
    if some_list == []:
        return 0
    elif len(some_list) == 0:  # base case
        return some_list[0]
    else:
        return int(list_sum(some_list[1:])) + int(some_list[0]) # recursive case
# if some_list:
#         return some_list[0] + (list_sum(some_list[1:]) if len(some_list) > 1 else 0)
#     return 0
# a = input().split(" ")
# # print(a.split(" ") )
# print(list_sum(a))
