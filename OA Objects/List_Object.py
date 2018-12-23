import copy

class Listobject:
    name = ""
    short_description = ""
    list_text = ""

    def equals(self,tocompare):
        return ((self.name == tocompare.name) and (self.short_description == tocompare.short_description))

    def __init__(self,name,short_description):
        self.name = name
        self.short_description = short_description
        self.list_text = name
        if len(short_description) > 0:
            self.list_text += ' - ' + short_description
