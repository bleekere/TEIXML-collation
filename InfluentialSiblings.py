# import finding_parents
from finding_parents_method import finding_parents
# import lxml Element Tree
from lxml import etree as ElementTree
tree = ElementTree.parse("xml/liefde-tsa.xml")
root = tree.getroot()
# opvangen van actie:
firstPage = root.find(".//div[@type='page']")
# query firstPage met lxml (. is belangrijk, verwijst naar eerste div als root)
textNodes = firstPage.xpath(".//text()")
for textNode in textNodes:
    parents = finding_parents(textNode)
    # if value of @type = overwritten
    firstTag = next((tag for tag in parents if tag.get("type") == "overwritten"), None)
    if firstTag is not None and not textNode.is_tail:
        sibling = firstTag.getnext()
        if sibling.get("place") == "overwritten":
            print(textNode)
            continue
        else:
            continue
    firstTag = next((tag for tag in parents if tag.get("type") == "instant correction"), None)
    if firstTag is not None and not textNode.is_tail:
        sibling = firstTag.getnext()
        if sibling.get("place") == "overwritten":
            continue
        else:
            print(textNode)
            continue
    firstTag = next((tag for tag in parents if tag.get("place") == "overwritten"), None)
    if firstTag is not None and not textNode.is_tail:
        sibling = firstTag.getprevious()
        if sibling.get("type") == "overwritten":
            continue
        elif sibling.get("type") == "instant correction":
            print(textNode)
            continue
        else:
            continue
    firstTag = next((tag for tag in parents if tag.tag == "add"), None)
    if firstTag is not None and not textNode.is_tail:
        continue
    print(textNode)




