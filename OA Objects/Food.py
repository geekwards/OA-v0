import List_Object
import copy

class Foods:
    list_of_food = []
    all_food = []

    def add_new(self,food):
        self.all_food.append(food)
        self.list_of_food.append(List_Object.List_object(food.name,food.short_description))

    def remove(self,food):
        self.list_of_food.remove(self.list_of_food[self.all_food.index(self.get_food(food.name))])
        self.all_food.remove(self.get_food(food.name))

    def equals(self,tocompare):
        same = (len(self.all_food) == len(tocompare.all_food))
        if same:
            for idx,item in enumerate(tocompare.all_food):
                same = same and item.equals(self.all_food[idx])

        return same

    def clone(self):
        return copy.deepcopy(self)

    def isempty(self):
        return len(self.all_food) == 0

    def update(self,food):
        found = False
        for item in self.all_food:
            if item.name == food.name:
                idx = self.all_food.index(item)
                self.all_food[idx] = food
                self.list_of_food[idx].name = food.name
                self.list_of_food[idx].short_description = food.short_description
                found = True
                break
        
        if not found:
            self.add_new(food)

    def get_food(self,name):
        for item in self.all_food:
            if item.name == name:
                return item
        
        return Food('','')

    def __len__(self):
        return len(self.all_food)

    def __init__(self):
        self.all_food = []
        self.list_of_food = []

class Food:
    name = ''
    short_description = ''
    description = ''
    value = 0
    weight = 0

    def equals(self,tocompare):
        return ((self.name == tocompare.name)
            and (self.short_description == tocompare.short_description)
            and (self.description == tocompare.description)
            and (self.value == tocompare.value)
            and (self.weight == tocompare.weight)
            )

    def clone(self):
        return copy.deepcopy(self)

    def isempty(self):
        return (self.name.strip() == '' and self.short_description.strip() == '')

    def __init__(self,name,short_description=''):
        self.name = name
        self.short_description = short_description
