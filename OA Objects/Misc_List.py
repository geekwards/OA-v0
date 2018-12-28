import List_Object
import copy

class Misc_lists:
    list_of_lists = []
    all_lists = []

    def add_new(self,misc_list):
        self.all_lists.append(misc_list)
        self.list_of_lists.append(List_Object.List_object(misc_list.name,''))

    def remove(self,misc_list):
        self.list_of_lists.remove(self.list_of_lists[self.all_lists.index(self.get_misc_list(misc_list.name))])
        self.all_lists.remove(misc_list)

    def equals(self,tocompare):
        same = (len(self.all_lists) == len(tocompare.all_lists))
        if same:
            for idx,item in enumerate(tocompare.all_lists):
                same = same and item.equals(self.all_lists[idx])

        return same

    def clone(self):
        return copy.deepcopy(self)

    def isempty(self):
        return len(self.all_lists) == 0

    def update(self,misc_list):
        found = False
        for item in self.all_lists:
            if item.name == misc_list.name:
                idx = self.all_lists.index(item)
                self.all_lists[idx] = misc_list
                self.list_of_lists[idx].name = misc_list.name
                found = True
                break
        
        if not found:
            self.add_new(misc_list)

    def get_misc_list(self,name):
        for item in self.all_lists:
            if item.name == name:
                return item

    def __len__(self):
        return len(self.all_lists)

    def __init__(self):
        self.all_lists = []
        self.list_of_lists = []

class Misc_list:
    name = ''
    all_items = []

    def add_new(self,list_item):
        self.all_items.append(list_item)

    def remove(self,list_item):
        self.all_items.remove(list_item)

    def equals(self,tocompare):
        same = (self.name == tocompare.name)
        for idx,item in enumerate(self.all_items):
            same = same and (item == tocompare.all_items[idx])

        return same

    def clone(self):
        return copy.deepcopy(self)

    def __len__(self):
        return len(self.all_items)

    def __init__(self,name,misc_list):
        self.name = name
        self.all_items = misc_list
