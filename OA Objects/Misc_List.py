import Base_Object
import copy

class Misc_lists(Base_Object.Set_of_Items):
    pass

class Misc_list(Base_Object.Item):
    name = ''
    short_description = ''
    all_items = []
    item_names = []

    def add_new(self,list_item):
        self.all_items.append(list_item)
        self.item_names.append(list_item.name)

    def remove(self,list_item):
        self.all_items.remove(list_item)

    def __len__(self):
        return len(self.all_items)

    def __init__(self,name,short_description='',misc_list=[]):
        self.name = name
        self.short_description = short_description
        self.all_items = []
        self.item_names = []

        for idx,item in enumerate(misc_list):
            self.add_new(item)

