from lxml import etree
from lxml import etree
xml_string = input()
att = input()
# xml_string ='<a attr="123"><b>hello</b><c/></a>'
# att = 'attr'

root = etree.fromstring(xml_string)
# root = etree.parse(xml_string).getroot()
# etree.dump(root)
print(root.get(att))
# for a in root:
#     if a.get(att):
#         print(a.get(att))
# else:
#     # print("None")
#     pass