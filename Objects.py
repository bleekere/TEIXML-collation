# import finding_parents
from finding_parents_function import finding_parents
# import lxml Element Tree
from lxml import etree as ElementTree
from flowchart import FlowChartElement


def first_tag(text_node, *args):
    parents = finding_parents(text_node)
    del_tag = next((element for element in parents if element.tag == "del"), None)
    return del_tag is not None and not text_node.is_tail

def main():
    # XML inlezen in geheugen
    tree = ElementTree.parse("xml/liefde-tsa.xml")
    # element ophalen en opvangen van actie :
    root = tree.getroot()
    # tekstelementen van 3e zin van 1e pagina ophalen
    sentence_list= root.xpath(".//s[@n='B917_2bis_B5_tsA_Liefde,[003]']//text()")
    element_list = []
    for text_element in sentence_list:
        # create new instance from module "flowchart" by invoking constructor from FlowChartElement-class
        # store reference to instance in the variable "if_parent_has_tag_del"
        # initialize instance variable
        # function definition "first_tag" as parameter of the constructor
        if_parent_has_tag_del = FlowChartElement(first_tag)
        # evalueer of tekst element's parent del tag heeft
        if if_parent_has_tag_del.evaluate(text_element):
            # voeg tekst element toe aan lijst
            element_list.append(text_element)
    print(element_list)
main()





