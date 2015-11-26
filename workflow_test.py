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
    # input  = ts_a
    tree_tsa = ElementTree.parse("xml/liefde-tsa.xml")
    root_tsa = tree_tsa.getroot()
    first_page_tsa = root_tsa.xpath("./text//div[@n='01r']")
    # input = ts_b
    tree_tsb = ElementTree.parse("xml/liefde-tsb.xml")
    root_tsb = tree_tsb.getroot()
    first_page_tsb = root_tsb.xpath("./text//div[@n='01r']")
    # output ts_a en ts_b
    text_file_tsa = open("text_file_tsa", "w")
    text_file_tsb = open("text_file_tsb", "w")
    # bewerkingen ts_a
    visitor_tsa = XMLElementVisitor(text_file_tsa)
    traverser_tsa = XMLElementTraverser(visitor_tsa)
    traverser_tsa.traverse(first_page_tsa)
    # bewerkingen ts_b
    visitor_tsb = XMLElementVisitor(text_file_tsb)
    traverser_tsb = XMLElementTraverser(visitor_tsb)
    traverser_tsb.traverse(first_page_tsb)
    # output files sluiten
    text_file_tsa.close()
    text_file_tsb.close()



main()
