# This python file contains classes to build a flow chart
# author: Ronald Haentjens Dekker

class FlowChartElement(object):
    def __init__(self, predicate):
        self.predicate = predicate
        self.whenTrue = None
        self.whenFalse = None

    def evaluate(self, xml_text_element, *args):
        result = self.predicate(xml_text_element, args)
        if result:
            if not self.whenTrue:
                return True
            else:
                return self.whenTrue(xml_text_element, args)
        else:
            if not self.whenFalse:
                return False
            else:
                return self.whenFalse(xml_text_element, args)

    def when_true_call(self, workflow_element):
        self.whenTrue = workflow_element

    def when_false_call(self, workflow_element):
        self.whenFalse = workflow_element

