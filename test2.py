# import lxml library
from lxml import etree as ElementTree
file = open("country_data.xml")
data = file.read()
tree = ElementTree.fromstring(data)
rank = tree.xpath('.//rank')[0]
input = rank
output = []
while input != None:
    input = input.getparent()
    if input != None:
        output.append(input)
print(output)






