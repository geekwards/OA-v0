import copy

class Listobject:
    name = ""
    short_description = ""

    def clone(self):
        return copy.copy(self)

    def __init__(self,name,short_description):
        self.name = name
        self.short_description = short_description
