# import the library
from xml.dom.pulldom import START_ELEMENT, parse

doc = parse("xml/liefde.xml")
for event, node in doc:
    if event == START_ELEMENT and node.localName == "p":
        doc.expandNode(node)
        print(node.toxml())
