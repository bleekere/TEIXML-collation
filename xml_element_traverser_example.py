# XML Element Traverser example
# author: Ronald Haentjens Dekker
from lxml import etree as ElementTree
from xml_element_traverser import XMLElementTraverser


class XMLElementVisitor(object):
    def pre_visit_element(self, xml_element):
        return True

    def visit_element(self, xml_element):
        print("Opening tag: "+str(xml_element))

    def visit_text(self, text):
        print(text)

    def post_visit_element(self, xml_element):
        print("Closing tag: "+str(xml_element))


def main():
    tree = ElementTree.parse("xml/liefde-tsa.xml")
    root = tree.getroot()
    sentence = root.xpath(".//s[@n='B917_2bis_B5_tsA_Liefde,[003]']")
    visitor = XMLElementVisitor()
    traverser = XMLElementTraverser(visitor)
    traverser.traverse(sentence)


main()
