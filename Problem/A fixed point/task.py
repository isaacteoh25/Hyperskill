# mid = 0
def binarySearch(arr, n): 
    # global mid
    for i in range(n): 
        if arr[i] is i: 
            return True 
    # If no fixed point present then return -1 
    return False
  

# arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100] 
arr = [int(i) for i in input().split()]
n = len(arr)
 
print(str(binarySearch(arr, n)))
# print("Fixed Point is " + str(binarySearch(arr, 0, n-1)))
