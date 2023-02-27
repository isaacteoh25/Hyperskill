# put your python code here

numbers = input().split()
num1 = input()
# use a.index()
a = []
for n, month in enumerate(numbers):
    if month == num1:
        a.append(n)
if a == []:
    print("not found")
else:
    for i in a:
        print(i, end= " ")

line = input().split()
looking_num = input()
indexes = ' '.join([str(num_index) for num_index, num in enumerate(line) if num == looking_num])
\indexes if len(indexes) != 0 else 'not found')
