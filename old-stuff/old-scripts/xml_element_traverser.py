# XML Element Traverser
# Class for traversing a XML element tree using a visitor as a callback
# author: Ronald Haentjens Dekker
from enum import Enum

Iteration = Enum('Iteration', 'CONTINUE STOP')


class XMLElementTraverser(object):
    def __init__(self, xml_element_visitor):
        self.xml_element_visitor = xml_element_visitor

    def traverse(self, xml_element):
        for child in xml_element:
            if self.xml_element_visitor.pre_visit_element(child) == Iteration.CONTINUE:
                self.xml_element_visitor.visit_element(child)
                if child.text:
                    self.xml_element_visitor.visit_text(child.text)
                self.traverse(child)
                self.xml_element_visitor.post_visit_element(child)
            if child.tail:
                self.xml_element_visitor.visit_text(child.tail)

