from finding_parents_method import finding_parents
# import lxml library
from lxml import etree as ElementTree
# genereer data voor input later
file = open('country_data.xml')
data = file.read()
tree = ElementTree.fromstring(data)
rank = tree.xpath('.//rank')[0]

parents = finding_parents(rank)
print(parents)






