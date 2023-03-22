# n = int(input())
# name = []
# for i in range(n):
#     name.append(input())
# name = ["Kate","Mike", "Nick","Sam","Bob","Karl"]
# names = ["Alice", "Bob", "John", "Andrew"]

# def stableSelectionSort(a, n):
def sort_names(names):
    for k, z in enumerate(names):
        index = k
        for i, name in enumerate(names):
            if len(name) > len(z) and i > k:
                index = i
        names[k], names[index] = names[index], names[k]
    return names

def sort_names(elements):
    elements.sort(reverse=True, key=len)
    return elements

sort_names = (lambda n: sorted(n, key=len, reverse=True))

def sort_names(names):
    """Sort names by length in descending order."""
    for i in range(len(names) - 1):
        index = i

        for j in range(i + 1, len(names)):
            if len(names[j]) > len(names[index]):
                index = j

        x = names[index]
        names.remove(x)
        names.insert(i, x)
    return names
# def printArray(a, n):
    # for i in range(n):
    # #     print(a[i])
    #     print("%d" % a[i], end=" ")

    # Driver Code


# print(sort_names(name))
# a = [4, 5, 3, 2, 4, 1]
# n = len(name)
# stableSelectionSort(name, n)
# printArray(name, n)
