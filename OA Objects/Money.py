import List_Object
import copy

class Monies:
    list_of_money = []
    all_money = []

    def add_new(self,money):
        self.all_money.append(money)
        self.list_of_money.append(List_Object.List_object(money.name,money.short_description))

    def remove(self,money):
        self.list_of_money.remove(self.list_of_money[self.all_money.index(self.get_money(money.name))])
        self.all_money.remove(self.get_money(money.name))

    def equals(self,tocompare):
        same = (len(self.all_money) == len(tocompare.all_money))
        if same:
            for idx,item in enumerate(tocompare.all_money):
                same = same and item.equals(self.all_money[idx])

        return same

    def clone(self):
        return copy.deepcopy(self)

    def isempty(self):
        return len(self.all_money) == 0

    def update(self,money):
        found = False
        for item in self.all_money:
            if item.name == money.name:
                idx = self.all_money.index(item)
                self.all_money[idx] = money
                self.list_of_money[idx].name = money.name
                self.list_of_money[idx].short_description = money.short_description
                found = True
                break
        
        if not found:
            self.add_new(money)

    def get_money(self,name):
        for item in self.all_money:
            if item.name == name:
                return item
        
        return Money('','')

    def __len__(self):
        return len(self.all_money)

    def __init__(self):
        self.all_money = []
        self.list_of_money = []

class Money:
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
