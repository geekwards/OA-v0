import Base_Equipment

class Weapons(Base_Equipment.Base_equipment):
    def add_new(self,item):
        if type(item) == Weapon and not(item.isempty()):
            super().add_new(item)
        else:
            raise ValueError('expected Weapon object, instead got ' + str(type(item)))

    def __eq__(self,tocompare):
        if type(tocompare) == Weapons and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Weapons object, instead got ' + str(type(tocompare)))

class Weapon(Base_Equipment.Equip):
    hands = 0
    weapon_type = ''
    range = 0
    ammo_type = ''
    damage_types = []

    def __eq__(self,tocompare):
        if type(tocompare) == Weapon and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Weapon object, instead got ' + str(type(tocompare)))

    def __init__(self,name,short_description=''):
        self.damage_types = []
        super().__init__(name,short_description)