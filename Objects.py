# import finding_parents
from finding_parents_function import finding_parents
# import lxml Element Tree
from lxml import etree as ElementTree
from flowchart import FlowChartElement
def firstTag(textNode, *args):
    parents = finding_parents(textNode)
    delTag = next((element for element in parents if element.tag == "del"), None)
    return delTag is not None and not textNode.is_tail

def main():
    tree = ElementTree.parse("xml/liefde-tsa.xml")
    root = tree.getroot()
    # opvangen van actie:
    sentenceList= root.xpath(".//div[@type='page']/p/s[2]/text()")
    example = sentenceList[0]
    if_parent_has_tag_del = FlowChartElement(firstTag)
    print(if_parent_has_tag_del.evaluate(example))

main()





