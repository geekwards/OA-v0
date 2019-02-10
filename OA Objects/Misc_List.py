import Base_Object
import List_Object
import copy

class Misc_lists(Base_Object.Set_of_Items):
    def add_new(self,item):
        if type(item) == Misc_list and not(item.isempty()):
            super().add_new(item)
        else:
            raise ValueError('expected Misc_list object, instead got ' + str(type(item)))

    def __eq__(self,tocompare):
        if type(tocompare) == Misc_lists and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Misc_lists object, instead got ' + str(type(tocompare)))

class Misc_list(Base_Object.Item):
    name = ''
    short_description = ''
    all_items = []
    item_names = []

    def add_new(self,list_item):
        if type(list_item) == List_Object.List_object:
            self.all_items.append(list_item)
            self.item_names.append(list_item.name)
        else:
            raise ValueError('expected List_object object, instead got ' + str(type(list_item)))

    def remove(self,list_item):
        self.all_items.remove(list_item)

    def get_item(self,name):
        for item in self.all_items:
            if item.name == name:
                return item
        
        return List_Object.List_object('','')

    def __eq__(self,tocompare):
        if type(tocompare) == Misc_list and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Misc_list object, instead got ' + str(type(tocompare)))

    def __len__(self):
        return len(self.all_items)

    def __init__(self,name,short_description='',misc_list=[]):
        self.name = name
        self.short_description = short_description
        self.all_items = []
        self.item_names = []

        for idx,item in enumerate(misc_list):
            self.add_new(item)

