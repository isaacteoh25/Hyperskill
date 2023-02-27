n = int(input())
name = []
for i in range(n):
    name.append(input())
# name = ["Kate","Mike", "Nick","Sam","Bob","Karl"]

def stableSelectionSort(a, n):
    # Traverse through all array elements
    for i in range(n):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if len(a[min_idx]) > len(a[j]):
                min_idx = j

                # Move minimum element at current i
        key = a[min_idx]
        while min_idx > i:
            a[min_idx] = a[min_idx - 1]
            min_idx -= 1
        a[i] = key


def printArray(a, n):
    for i in range(n):
        print(a[i])
        # print("%d" % a[i], end=" ")

    # Driver Code


# a = [4, 5, 3, 2, 4, 1]
n = len(name)
stableSelectionSort(name, n)
printArray(name, n)

print(*sorted([input() for _ in range(int(input()))], key=len), sep="\n")