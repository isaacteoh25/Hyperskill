from lxml import etree

# xml_string = input()
xml_string ='<a attr="123"><b>hello</b><c/></a>'
# att = 'attr'

root = etree.fromstring(xml_string)
# root = etree.parse(xml_string).getroot()
# etree.dump(root)
# print(root.get(att))
print(str(len(root)) + " " + str(len(root.keys())))
print(len(list(root)), len(root.keys()))