def check_email(string):
    index = string.find("@") + 1
    if " " not in string and "@" in string and "@." not in string and string.find(".", index) >= 1:
        return "True"
    else:
        return "False"

def check_email(string):
    return all([' ' not in string, '@' in string, '.' in string[string.find('@') + 2:]])


def check_email(string):
    return bool("@" in string and "." in string[string.find(
        "@"):] and ".@" not in string and "@." not in string and " " not in string)
