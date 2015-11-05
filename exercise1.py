import xml.etree.ElementTree as ET
tree = ET.parse("xml/liefde.xml")
root = tree.getroot()


x = root.find("./text/body/div/div/p")

print(x)


