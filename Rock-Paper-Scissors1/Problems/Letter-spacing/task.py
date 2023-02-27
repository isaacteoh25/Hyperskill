text = input()
number = int(input())
print(*text, sep=(number * ' '))
# print(*list(input()), sep=' ' * int(input()))