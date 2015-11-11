# import lxml library
from lxml import etree as ElementTree
file = open("country_data.xml")
data = file.read()
tree = ElementTree.fromstring(data)
rank = tree.xpath('.//rank')[0]
x = rank
while x != None:
    x = x.getparent()
    if x != None:
        print(x.tag)

