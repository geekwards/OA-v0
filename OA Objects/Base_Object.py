import List_Object
import copy

class Set_of_Items:
    list_of_items = []
    all_items = []

    def add_new(self,item):
        self.all_items.append(item)
        self.list_of_items.append(List_Object.List_object(item.name,item.short_description))

    def remove(self,item):
        self.list_of_items.remove(self.list_of_items[self.all_items.index(self.get_item(item.name))])
        self.all_items.remove(self.get_item(item.name))

    def clone(self):
        return copy.deepcopy(self)

    def isempty(self):
        return len(self.all_items) == 0

    def update(self,item):
        found = False
        for itm in self.all_items:
            if item.name == itm.name:
                idx = self.all_items.index(itm)
                self.all_items[idx] = item
                self.list_of_items[idx].name = item.name
                self.list_of_items[idx].short_description = item.short_description
                found = True
                break
        
        if not found:
            self.add_new(item)

    def get_item(self,name):
        for item in self.all_items:
            if item.name == name:
                return item
        
        return Item('','')

    def __eq__(self,tocompare):
        same = (len(self.all_items) == len(tocompare.all_items))
        if same:
            for idx,item in enumerate(tocompare.all_items):
                same = same and item == self.all_items[idx]

        return same

    def __len__(self):
        return len(self.all_items)

    def __init__(self):
        self.all_items = []
        self.list_of_items = []

class Item:

    def clone(self):
        return copy.deepcopy(self)

    def isempty(self):
        return (self.name.strip() == '' and self.short_description.strip() == '')

    def __eq__(self,tocompare):
        return self.__dict__ == tocompare.__dict__

    def __init__(self,name,short_description=''):
        self.name = name
        self.short_description = short_description
 