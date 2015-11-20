# een eerste test om door de flowchart te lopen
from lxml import etree as ElementTree
from xml_element_traverser import XMLElementTraverser, Iteration


class XMLElementVisitor(object):
    def pre_visit_element(self, xml_element):
        print("Visiting tag: "+str(xml_element))
        if xml_element.tag == "del":
            if xml_element.get("type") == "overwritten":
                if xml_element.getnext().get("place") == "overwritten":
                    return Iteration.CONTINUE
                else:
                    if xml_element.get("type") == "instant correction":
                        if xml_element.getnext().get("place") == "overwritten":
                            return Iteration.STOP
                        else:
                            return Iteration.CONTINUE
            else:
                return Iteration.CONTINUE
        else:
            if xml_element.tag == "add":
                if xml_element.get("place") == "overwritten":
                    if xml_element.getprevious().get("type") == "overwritten":
                        return Iteration.STOP
                    else:
                        return Iteration.CONTINUE
                else:
                    return Iteration.STOP
            else:
                return Iteration.CONTINUE


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

