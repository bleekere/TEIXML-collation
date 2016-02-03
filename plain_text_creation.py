# een eerste test om door de flowchart te lopen
from lxml import etree as ElementTree
from xml_element_traverser import XMLElementTraverser, Iteration
import re

class XMLElementVisitor(object):
    # define explicit constructor (overruling the default constructur) with one parameter
    def __init__(self, plain_text_file):
        # assign parameter to property of class
        self.plain_text_file = plain_text_file
    def pre_visit_element(self, xml_element):
        if xml_element.tag == "del":
            if xml_element.get("type") == "overwritten" and xml_element.getnext().get("place") != "overwritten":
                return Iteration.STOP
            elif xml_element.get("type") == "instant correction" and xml_element.getnext().get("place") == "overwritten":
                return Iteration.STOP
        elif xml_element.tag == "add":
            if xml_element.get("place") != "overwritten":
                return Iteration.STOP
            elif xml_element.get("place") == "overwritten" and xml_element.getprevious().get("type") == "overwritten":
                return Iteration.STOP
        elif xml_element.tag == "unclear" and xml_element.getprevious() is not None and xml_element.getprevious().tag == "unclear":
            return Iteration.STOP
        elif xml_element.tag == "note" or xml_element.tag == "metamark":
            return Iteration.STOP
        return Iteration.CONTINUE


    def visit_element(self, xml_element):
        if xml_element.tag == "lb":
            self.plain_text_file.write("\n")

    def visit_text(self, text):
        # compile all strings with two or more whitespaces (s = whitespace class met lb, taps, etc)
        pattern = re.compile(r'\s+')
        # replace the occurances of the pattern with the replacement ' ' and return the string
        normalised_text = re.sub(pattern,' ', text)
        self.plain_text_file.write(normalised_text)

    def post_visit_element(self, xml_element):
        pass


def main():
    input_file = "xml/tsq-test-small.xml"
    output_file = "xml/plain-text-tsq.txt"
    collate_groundlayer(input_file, output_file)


def collate_groundlayer(input_file, output_file):
    parser = ElementTree.XMLParser(remove_comments=True, remove_blank_text=True)
    tree = ElementTree.parse(input_file, parser)
    root = tree.getroot()
#   selected_text = root.xpath("./text//%s" % collation_input)
    text_file = open(output_file, 'w')
    visitor = XMLElementVisitor(text_file)
    traverser = XMLElementTraverser(visitor)
    traverser.traverse(root)
    text_file.close()


main()

