import List_Object
import copy 

class Armors:
    list_of_armors = []
    all_armors = []

    def add_new(self,armor):
        self.all_armors.append(armor)
        self.list_of_armors.append(List_Object.List_object(armor.name,armor.short_description))

    def remove(self,armor):
        self.list_of_armors.remove(self.list_of_armors[self.all_armors.index(self.get_armor(armor.name))])
        self.all_armors.remove(self.get_armor(armor.name))

    def equals(self,tocompare):
        same = (len(self.all_armors) == len(tocompare.all_armors))
        if same:
            for idx,item in enumerate(tocompare.all_armors):
                same = same and item.equals(self.all_armors[idx])

        return same

    def clone(self):
        return copy.deepcopy(self)

    def isempty(self):
        return len(self.all_armors) == 0

    def update(self,armor):
        found = False
        for item in self.all_armors:
            if item.name == armor.name:
                idx = self.all_armors.index(item)
                self.all_armors[idx] = armor
                self.list_of_armors[idx].name = armor.name
                self.list_of_armors[idx].short_description = armor.short_description
                found = True
                break
        
        if not found:
            self.add_new(armor)

    def get_armor(self,name):
        for item in self.all_armors:
            if item.name == name:
                return item
        
        return Armor('','')

    def __len__(self):
        return len(self.all_armors)

    def __init__(self):
        self.all_armors = []
        self.list_of_armors = []

class Armor:
    name = ''
    short_description = ''
    description = ''
    value = 0
    weight = 0
    health = 0
    capacity = 0
    special = ''
    damage_types = []

    def equals(self,tocompare):
        return ((self.name == tocompare.name)
            and (self.short_description == tocompare.short_description)
            and (self.description == tocompare.description)
            and (self.value == tocompare.value)
            and (self.weight == tocompare.weight)
            and (self.health == tocompare.health)
            and (self.capacity == tocompare.capacity)
            and (self.special == tocompare.special)
            and (self.damage_types == tocompare.damage_types)
            )

    def clone(self):
        return copy.deepcopy(self)

    def isempty(self):
        return (self.name.strip() == '' and self.short_description.strip() == '')

    def __init__(self,name,short_description=''):
        self.name = name
        self.short_description = short_description
