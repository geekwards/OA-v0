import copy

class List_Objects:
    list_of_list_objects = []
    all_list_objects = []

    def add_new(self,list_object):
        self.all_list_objects.append(list_object)
        self.list_of_list_objects.append(List_Object.Listobject(list_object))

    def remove(self,list_object):
        self.list_of_list_objects.remove(self.get_list_item(self.all_list_objects.index(list_object)))
        self.all_list_objects.remove(list_object)

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
        return len(self.all_list_objects) == 0

    def get_all(self):
        return self.all_list_objects

    def get_list(self):
        return self.list_of_list_objects

    def get_list_item(self,idx):
        return self.list_of_list_objects[idx]

    def update(self,idx,list_object):
        if (idx == None) or (idx > len(self.all_list_objects)-1):
            self.add_new(list_object)
        else:
            self.all_list_objects[idx] = list_object
            self.list_of_list_objects[idx].name = list_object.name

    def __getitem__(self,idx):
        if idx == None:
            return list_object('','')
        else:
            return self.all_list_objects[idx]

    def __init__(self):
        self.all_list_objects = []
        self.list_of_list_objects = []

class Listobject:
    name = ""
    short_description = ""

    def clone(self):
        return copy.copy(self)

    def __init__(self,name,short_description):
        self.name = name
        self.short_description = short_description
