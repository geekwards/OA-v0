import List_Object
import copy

class Misc_equipment:
    list_of_misc_equipment = []
    all_misc_equipment = []

    def add_new(self,stuff):
        self.all_misc_equipment.append(stuff)
        self.list_of_misc_equipment.append(List_Object.List_object(stuff.name,stuff.short_description))

    def remove(self,stuff):
        self.list_of_misc_equipment.remove(self.list_of_misc_equipment[self.all_misc_equipment.index(self.get_stuff(stuff.name))])
        self.all_misc_equipment.remove(self.get_stuff(stuff.name))

    def equals(self,tocompare):
        same = (len(self.all_misc_equipment) == len(tocompare.all_misc_equipment))
        if same:
            for idx,item in enumerate(tocompare.all_misc_equipment):
                same = same and item.equals(self.all_misc_equipment[idx])

        return same

    def clone(self):
        return copy.deepcopy(self)

    def isempty(self):
        return len(self.all_misc_equipment) == 0

    def update(self,stuff):
        found = False
        for item in self.all_misc_equipment:
            if item.name == stuff.name:
                idx = self.all_misc_equipment.index(item)
                self.all_misc_equipment[idx] = stuff
                self.list_of_misc_equipment[idx].name = stuff.name
                self.list_of_misc_equipment[idx].short_description = stuff.short_description
                found = True
                break
        
        if not found:
            self.add_new(stuff)

    def get_stuff(self,name):
        for item in self.all_misc_equipment:
            if item.name == name:
                return item
        
        return Stuff('','')

    def __len__(self):
        return len(self.all_misc_equipment)

    def __init__(self):
        self.all_misc_equipment = []
        self.list_of_misc_equipment = []

class Stuff:
    name = ''
    short_description = ''
    description = ''
    value = 0
    weight = 0
    health = 0
    capacity = 0
    special = ''

    def equals(self,tocompare):
        return ((self.name == tocompare.name)
            and (self.short_description == tocompare.short_description)
            and (self.description == tocompare.description)
            and (self.value == tocompare.value)
            and (self.weight == tocompare.weight)
            and (self.health == tocompare.health)
            and (self.capacity == tocompare.capacity)
            and (self.special == tocompare.special)
            )

    def clone(self):
        return copy.deepcopy(self)

    def isempty(self):
        return (self.name.strip() == '' and self.short_description.strip() == '')

    def __init__(self,name,short_description=''):
        self.name = name
        self.short_description = short_description
