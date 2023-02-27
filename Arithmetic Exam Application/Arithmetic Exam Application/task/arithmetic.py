# write your code here
a = input().split(" ")
b = a[1]
if b == "-":
    print(f"{int(a[0]) - int(a[2])}")
elif b == "+":
    print(f"{int(a[0]) + int(a[2])}")
else:
    print(f"{int(a[0]) * int(a[2])}")