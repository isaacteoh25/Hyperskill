# the follwing line reads the list from the input, do not modify it, please
passwords = input().split()
z = [print(x, len(x)) for x in sorted(passwords, key=len)]
# your code below
passwords.sort(key=len)
print(*[p + ' ' + str(len(p)) for p in passwords], sep='\n')
[print(i, len(i)) for i in passwords]
for password in passwords:
    print(password + " "+str(len(password)))

