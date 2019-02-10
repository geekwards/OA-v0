import copy

class List_object:
    name = ''
    short_description = ''
    list_text = ''

    def __eq__(self,tocompare):
        return ((self.name == tocompare.name) and (self.short_description == tocompare.short_description))

    def __lt__(self,tocompare):
        return (self.name<tocompare.name)

    def __init__(self,name,short_description=''):
        self.name = name
        self.short_description = short_description
        if len(short_description) > 0:
            self.list_text = name + ' - ' + short_description
        else:
            self.list_text = name
