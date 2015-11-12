# import finding_parents
from finding_parents_method import finding_parents
# import lxml Element Tree
from lxml import etree as ElementTree
tree = ElementTree.parse("xml/liefde-tsa.xml")
root = tree.getroot()
# opvangen van actie:
firstPage = root.find(".//div[@type='page']")
# query firstPage met lxml (. is belangrijk, verwijst naar eerste div als root)
textelements = firstPage.xpath(".//text()")
for textelement in textelements:
    parents = finding_parents(textelement)
    first_or_default = next((tag for tag in parents if tag.get("place") == "overwritten"), None)
    if first_or_default != None and not textelement.is_tail:
        print(textelement)
    # if value of type = instantcorrection
    # type = textelement.getparent().get('type')
    # if type == 'instant correction':
      #  print(type)
    #  if textelement.getparent().getnext().tag == "add":
    #   print()




