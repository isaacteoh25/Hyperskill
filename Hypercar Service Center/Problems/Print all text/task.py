from lxml import etree
# xml_string = input()
xml_string = "<root><elem1>I am elem1</elem1><elem2>I am elem2</elem2><elem3>I am elem3</elem3></root>"
root = etree.fromstring(xml_string)
# root = etree.parse(xml_string).getroot()
etree.dump(root)
# states = root[0]
# print(states)
for state in root:
    print(state.text)
