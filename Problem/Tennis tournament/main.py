n = int(input())

win_matches = []
matches = []
for _x in range(n):
    matches = input().split()
    if matches[1] == "win":
        win_matches.append(matches[0])

print(f"""{win_matches}
{len(win_matches)}""")
