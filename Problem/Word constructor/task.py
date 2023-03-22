inp1 = list(input())
inp2 = list(input())
# inp1 = "mo"
# inp2 = "ew"
for i, j in zip(inp1, inp2):
    print(i + j, end="")
result = ''
for i, j in zip(inp1, inp2):
    result += i + j
print(result)
a = [''.join(map(str, i)) for i in zip(inp1, inp2)]
print(''.join(a))
    # for a[0], a[1] in zip(a):
    #     print(a[0] + a[1])

for first, second in zip(inp1, inp2):
    print(first, second, sep="", end="")


new_word = []
for a, b in zip(inp1, inp2):
    new_word.append(a + b)
print("".join(new_word))
# or
print(*new_word, sep='')

res = []
for i, j in zip(inp1, inp2):
    res.extend([i, j])

print(''.join(res))
print(''.join((c1 + c2) for c1, c2 in zip(inp1, inp2)))

for i in zip(inp1, inp2):
    for j in i:
        print(j, end='')