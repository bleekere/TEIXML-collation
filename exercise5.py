# import finding_parents
from finding_parents_method import finding_parents
# import lxml Element Tree
from lxml import etree as ElementTree
tree = ElementTree.parse("xml/liefde-tsa.xml")
root = tree.getroot()
# opvangen van actie:
firstPage = root.find(".//div[@type='page']")
# query firstPage met lxml (. is belangrijk, verwijst naar eerste div als root)
textElements = firstPage.xpath(".//text()")
for textElement in textElements:
    parents = finding_parents(textElement)
    # if value of @place = overwritten
    first_or_default = next((tag for tag in parents if tag.get("place") == "overwritten"), None)
    if first_or_default is not None and not textElement.is_tail:
    # spring uit de lus met continue
        continue
    # first_or_default nu alle tags met value of @type = instantcorrection
    # first_or_default = next((tag for tag in parents if tag.get ("type") == "instant correction"), None)
    # sibling = first_or_default.getnext()
    # if sibling.get()
    # if first_or_default is not None and not textelement.is_tail:

    # else:
    # print(textelement)





