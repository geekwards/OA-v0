import copy

class Listobject:
    name = ""
    short_description = ""

    def clone(self):
        return copy.copy(self)

    def equals(self,tocompare):

        return ((self.name == tocompare.name) and (self.short_description == tocompare.short_description))

    def __init__(self,name,short_description):
        self.name = name
        self.short_description = short_description
