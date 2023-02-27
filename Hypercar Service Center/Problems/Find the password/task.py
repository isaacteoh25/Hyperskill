from lxml import etree
from lxml import etree
# xml_string = input()
# att = input()
# xml_string ='<profile><account login="login" password="secret"/></profile>'
# att = 'attr'


# print(root.get(att))
def find_password(xml_string):
    att = 'password'
    root = etree.fromstring(xml_string)
    for a in root:
        if a.get(att):
            return a.get(att)


# find_password(xml_string)