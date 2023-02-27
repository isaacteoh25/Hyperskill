import re


# put your regex in the variable template
# template = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,20}$"
template = "^([A-Z]{2})[' ']{0,}([\d]{2})[' ']{0,}([A-Z]{2})[' ']{0,}([\d]{4})$"
template = r"[A-Z]{2} ?\d{2} ?[A-Z]{2} ?\d{4}$"
template = r"^[A-Z]{2}\s?\d{2}\s?[A-Z]{2}\s?\d{4}$"
# print(re.match(template, "<start></start><start></start>"))
# print(re.match(template, "MH 10 EL 531114"))
# print(re.match(template, "HG77GH2037"))
# print(re.match(template, "MH 10 EL 5311"))