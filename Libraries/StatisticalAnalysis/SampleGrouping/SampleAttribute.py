

class SampleAttribute:

    def __init__(self):
        self.AttributeName = ''
        self.AttributeValue = ''

    def setAttributeName(self, attributeName):
        self.AttributeName = attributeName

    def setAttributeValue(self, attributeValue):
        self.AttributeValue = attributeValue

    def getAttributeName(self):
        return self.AttributeName

    def getAttributeValue(self):
        return self.AttributeValue