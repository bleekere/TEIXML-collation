# import lxml library
from lxml import etree as ElementTree
# genereer data voor input later
file = open('country_data.xml')
data = file.read()
tree = ElementTree.fromstring(data)
rank = tree.xpath('.//rank')[0]


def finding_parents(input):
    # maak een lege lijst
    output = []
    # get parent of input
    while input != None:
        input = input.getparent()
        # wanneer input geen parent heeft (root bereikt bij parent=None)
        if input != None:
            output.append(input)
    return output

parents = finding_parents(rank)
print(parents)






