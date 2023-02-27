# y = int(input('Enter  column:\n' ))
# x = int(input('Enter  row:\n'))
y = int(input())
x = int(input())

if (x not in range(1, 9)) or (y not in range(1, 9)):
    print('Entries not valid.\nEnter 1 - 8 only')
elif (y in range(2, 8)) and (x in range(2, 8)):
    # print('Moves = 8')
    print(8)
elif (y + x == 2) or(y + x == 9) or (y + x == 16):
    print(3)
else:
    print(5)

x, y = int(input()), int(input())


def valid_cell(col, row):
    if 1 <= col <= 8 and 1 <= row <= 8:
        return True
    return False


counter = 0

for i in range(x - 1, x + 2):
    for j in range(y - 1, y + 2):
        if valid_cell(i, j) and (i, j) != (x, y):
            counter += 1

print(counter)
