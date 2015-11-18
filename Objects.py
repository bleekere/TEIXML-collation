# import finding_parents
from finding_parents_method import finding_parents
# import lxml Element Tree
from lxml import etree as ElementTree
tree = ElementTree.parse("xml/liefde-tsa.xml")
root = tree.getroot()
# opvangen van actie:
sentenceList= root.xpath(".//div[@type='page']/p/s")
# query firstPage met lxml (. is belangrijk, verwijst naar eerste div als root)
print(ElementTree.dump(sentenceList[2]))
