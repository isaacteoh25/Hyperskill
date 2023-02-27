import re


# put your regex in the variable template
template = '([0-9]{1,2})[\/|\.]([0-9]{1,2})[\/|\.]([0-9]{4})'
string = input()
# compare the string and the template
result = re.match(template, string)
# print(result)
if result:
    print(result.group(3))
else:
    print(None)

template = r"(\d?\d[./]){2}(\d{4})"
string = input()
if re.match(template, string):
    print(re.match(template, string).group(2))
else:
    print('None')