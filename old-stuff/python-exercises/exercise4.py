# import the tree library
import xml.etree.ElementTree as ET
# specify the selection
tree = ET.parse("xml/liefde-tsa.xml")
root = tree.getroot()
# opvangen van actie:
x = root.find(".//div[@type='page']")
# iterate selection
y = x.iter()
# for each node (or element) in the y-selection, print the tag
for node in y:
    print(node.tag)


