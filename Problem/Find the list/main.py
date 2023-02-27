import re

# put your regex in the variable template
template = r'([0-9]*\)\s\w*\s[0-9])'
# template = r"(\d+\) \w+ \d+)+"
# template = r"((\d){1,}(\)){1}( ){1}(\w){1,}( ){1}(\d){1,}){1,}"
# template = r"(\d\)\s)(\w+)(\s\d)"
# template = r"\d+\) (\w+\s)+\d+"
# I thought a code below was correct, but not :(
# template = r'(\d+\) (\w+\s)+)+\d+\) (\w+\s)*\w+$'
result = re.match(template, '1) Curiosity 2) Perseverance 3) ?.')
# if result:
#     print(re.match(template, string).group(2))
# else:
#     print('None')
print(result)