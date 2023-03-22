# n, m = [int(dim) for dim in input().split()]
# matr = [list(input()) for _ in range(n)]
#
# x, y = [int(dim) for dim in input().split()]
# patt = [list(input()) for _ in range(x)]
#
#
# def contains2d(text, pattern):
#     for row in range(n):
#         for s in range(m - y + 1):
#             if text[row][s:y + s] == pattern[0]:
#                 if [fr[s:y + s] for fr in text[row:row + x]] == pattern:
#                     return True
#     return False
#
#
# print(contains2d(matr, patt))

import numpy as np

def czek():
    for i in range(x1 - x2 + 1):
        for j in range(y1 - y2 + 1):
            cmp = text[i:i + x2, j:j + y2] == pattern
            if cmp.all():
                return True
    return False

x1, y1 = map(int, input().split())
text = np.array([[int(y) for y in input()] for _ in range(x1)])
x2, y2 = map(int, input().split())
pattern = np.array([[int(y) for y in input()] for _ in range(x2)])
print(czek())


def contains2d(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(text[0]) - len(pattern[0]) + 1):
            row_sliced = text[i:i + len(pattern)]
            col_sliced = [n[j:j + len(pattern[0])] for n in row_sliced]

            if col_sliced == pattern:
                return True
    return False


text_matrix, pattern_matrix = [], []
row_txt, col_txt = map(int, input().split())

for _ in range(row_txt):
    text_matrix.append(list(input()))
row_pattern, col_pattern = map(int, input().split())
for _ in range(row_pattern):
    pattern_matrix.append(list(input()))

print(contains2d(text_matrix, pattern_matrix))