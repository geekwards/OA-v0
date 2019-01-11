import List_Object
import copy

class Clothing:
    list_of_clothing = []
    all_clothing = []

    def add_new(self,garment):
        self.all_clothing.append(garment)
        self.list_of_clothing.append(List_Object.List_object(garment.name,garment.short_description))

    def remove(self,garment):
        self.list_of_clothing.remove(self.list_of_clothing[self.all_clothing.index(self.get_garment(garment.name))])
        self.all_clothing.remove(self.get_garment(garment.name))

    def equals(self,tocompare):
        same = (len(self.all_clothing) == len(tocompare.all_clothing))
        if same:
            for idx,item in enumerate(tocompare.all_clothing):
                same = same and item.equals(self.all_clothing[idx])

        return same

    def clone(self):
        return copy.deepcopy(self)

    def isempty(self):
        return len(self.all_clothing) == 0

    def update(self,garment):
        found = False
        for item in self.all_clothing:
            if item.name == garment.name:
                idx = self.all_clothing.index(item)
                self.all_clothing[idx] = garment
                self.list_of_clothing[idx].name = garment.name
                self.list_of_clothing[idx].short_description = garment.short_description
                found = True
                break
        
        if not found:
            self.add_new(garment)

    def get_garment(self,name):
        for item in self.all_clothing:
            if item.name == name:
                return item
        
        return Garment('','')

    def __len__(self):
        return len(self.all_clothing)

    def __init__(self):
        self.all_clothing = []
        self.list_of_clothing = []

class Garment:
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
