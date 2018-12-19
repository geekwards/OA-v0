import List_Object
import copy

class Misclists:
    list_of_misc_lists = []
    all_misc_lists = []

    def add_new(self,misc_list):
        self.all_misc_lists.append(misc_list)
        self.list_of_misc_lists.append(List_Object.Listobject(misc_list.name,''))

    def remove(self,misc_list):
        self.list_of_misc_lists.remove(self.get_picklist_item(self.all_misc_lists.index(misc_list)))
        self.all_misc_lists.remove(misc_list)

    def clone(self):
        return copy.copy(self)

    def equals(self,tocompare):
        same = True

        same = (len(self.get_all()) == len(tocompare.get_all()))

        if same:
            for idx,item in enumerate(tocompare.get_all()):
                same = same and item.equals(self.get_all()[idx])

        return same

    def isempty(self):
        return len(self.all_misc_lists) == 0

    def get_all(self):
        return self.all_misc_lists

    def get_picklist(self):
        return self.list_of_misc_lists

    def get_picklist_item(self,idx):
        return self.list_of_misc_lists[idx]

    def update(self,idx,misc_list):
        if (idx == None) or (idx > len(self.all_misc_lists)-1):
            self.add_new(misc_list)
        else:
            self.all_misc_lists[idx] = misc_list
            self.list_of_misc_lists[idx].name = misc_list.name

    def get_list(self,name):
        for item in self.all_misc_lists:
            if item.name == name:
                return item

    def __getitem__(self,idx):
        if idx == None:
            return Misclist('',[])
        else:
            return self.all_misc_lists[idx]

    def __len__(self):
        return len(self.all_misc_lists)

    def __init__(self):
        self.all_misc_lists = []
        self.list_of_misc_lists = []

class Misclist:
    name = ""
    misc_list = []

    def clone(self):
        return copy.copy(self)

    def equals(self,tocompare):
        same = True

        same = same and (self.name == tocompare.name)
        for idx,item in enumerate(self.get_list()):
            same and (item == tocompare.get_list()[idx])

        return same

    def add_new(self,list_item):
        self.misc_list.append(list_item)

    def remove(self,list_item):
        self.misc_list.remove(list_item)

    def get_list(self):
        return self.misc_list

    def __init__(self,name,list):
        self.name = name
        self.misc_list = list
