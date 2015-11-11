# import lxml Element Tree
from lxml import etree as ElementTree
tree = ElementTree.parse("xml/liefde-tsa.xml")
root = tree.getroot()
# opvangen van actie:
firstPage = root.find(".//div[@type='page']")
# query firstPage met lxml (. is belangrijk, verwijst naar eerste div als root)
textelements = firstPage.xpath(".//text()")
for textelement in textelements:
    # if value of place == overwritten, ignore text and tag
    place = textelement.getparent().get('place')
    if place == "overwritten" and textelement.is_tail == False:
        pass
    else:
        print(textelement)




