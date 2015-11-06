# import the tree library
import xml.etree.ElementTree as ET
# import the pull dom library
from xml.dom.pulldom import START_ELEMENT, parse
# specify the selection
tree = ET.parse("xml/liefde-tsa.xml")
root = tree.getroot()
# opvangen van actie:
x = root.find(".//div[@type='page']")
print(x)



# doc = parse("xml/liefde-tsa.xml")
# for event, node in doc:
  #  if event == START_ELEMENT and node.localName == "p":
   #     doc.expandNode(node)
    #    print(node.toxml())
