import List_Object
import copy

class Weapons:
    list_of_weapons = []
    all_weapons = []

    def add_new(self,weapon):
        self.all_weapons.append(weapon)
        self.list_of_weapons.append(List_Object.List_object(weapon.name,weapon.short_description))

    def remove(self,weapon):
        self.list_of_weapons.remove(self.list_of_weapons[self.all_weapons.index(self.get_weapon(weapon.name))])
        self.all_weapons.remove(self.get_weapon(weapon.name))

    def equals(self,tocompare):
        same = (len(self.all_weapons) == len(tocompare.all_weapons))
        if same:
            for idx,item in enumerate(tocompare.all_weapons):
                same = same and item.equals(self.all_weapons[idx])

        return same

    def clone(self):
        return copy.deepcopy(self)

    def isempty(self):
        return len(self.all_weapons) == 0

    def update(self,weapon):
        found = False
        for item in self.all_weapons:
            if item.name == weapon.name:
                idx = self.all_weapons.index(item)
                self.all_weapons[idx] = weapon
                self.list_of_weapons[idx].name = weapon.name
                self.list_of_weapons[idx].short_description = weapon.short_description
                found = True
                break
        
        if not found:
            self.add_new(weapon)

    def get_weapon(self,name):
        for item in self.all_weapons:
            if item.name == name:
                return item
        
        return Weapon('','')

    def __len__(self):
        return len(self.all_weapons)

    def __init__(self):
        self.all_weapons = []
        self.list_of_weapons = []

class Weapon:
    name = ''
    short_description = ''
    description = ''
    value = 0
    weight = 0
    health = 0
    capacity = 0
    hands = 0
    weapon_type = ''
    range = 0
    ammo_type = ''
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
            and (self.hands == tocompare.hands)
            and (self.weapon_type == tocompare.weapon_type)
            and (self.range == tocompare.range)
            and (self.ammo_type == tocompare.ammo_type)
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
