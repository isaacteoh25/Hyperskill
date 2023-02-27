import re


# template = "\<[a-z]+\>[^<]{0,}\<\/[a-z]+\>$"

# template = '^<[a-z]{0,}>.*?</[a-z]{0,}>'
template = r'<[a-z]+>.*?</[a-z]+>'
print(re.match(template, "<start></start><start></start>"))
print(re.match(template, "<start></start>"))
print(re.match(template, "<start>a</start>"))