def merge_arrays(a, b):
    # "c" will contain the result of merging arrays "a" and "b"
    c = []
    while a or b:
        if not b or ((a and b)  and a[0] < b[0]):
            # removing the first element from "a" and adding it to "c"
            c.append(a[0])
            a.pop(0)
        else:
            # removing the first element from "b" and adding it to "c"
            c.append(b[0])
            b.pop(0)
    return c

# list_array = list(map(int, input().split()))
# list_arraya = [1, 2, 3]
# list_arrayb = [ 2, 3, 4, 4]
# count = 0
# print(merge_arrays(list_arraya, list_arrayb))