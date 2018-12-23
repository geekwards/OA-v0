import List_Object
import copy

class Misclists:
    list_of_lists = []
    all_lists = []

    def add_new(self,misc_list):
        self.all_misc_lists.append(misc_list)
        self.list_of_misc_lists.append(List_Object.Listobject(misc_list.name,''))

    def remove(self,misc_list):
        self.list_of_lists.remove(self.list_of_lists(self.all_lists.index(self(misc_list.name))))
        self.list_of_lists.remove(misc_list)

    def equals(self,tocompare):
        same = (len(self.get_all()) == len(tocompare.get_all()))
        if same:
            for idx,item in enumerate(tocompare.get_all()):
                same = same and item.equals(self.get_all()[idx])

        return same

    def clone(self):
        return copy.copy(self)

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
            self.add_new(archtype)

    def __len__(self):
        return len(self.all_lists)

    def __getitem__(self,name):
        for item in self.all_lists:
            if item.name == misc_list.name:
                return item

    def __init__(self):
        self.all_lists = []
        self.list_of_lists = []

class Misclist:
    name = ''
    all_items = []

    def add_new(self,list_item):
        self.misc_list.append(list_item)

    def remove(self,list_item):
        self.misc_list.remove(list_item)

    def equals(self,tocompare):
        same = (self.name == tocompare.name)
        for idx,item in enumerate(self.get_list()):
            same and (item == tocompare.get_list()[idx])

        return same

    def clone(self):
        return copy.copy(self)

    def __len__(self):
        return len(self.all_items)

    def __init__(self,name,misc_list):
        self.name = name
        self.all_items = misc_list
