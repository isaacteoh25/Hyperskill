import re


# put your regex in the variable template
# template = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,20}$"
template ='[A-Za-z0-9_-]{5,}$'
# r"[\w-]{5,}$"

# passwd = '126480~3'
# passwd = 'aAqwer-_'
#
# # compiling regex
# pat = re.compile(template)
#
# # searching regex
# mat = re.search(pat, passwd)
#
# # validating conditions
# if mat:
#     print("Password is valid.")
# else:
#     print("Password invalid !!")