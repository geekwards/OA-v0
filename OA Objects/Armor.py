import Base_Equipment

class Armors(Base_Equipment.Base_equipment):
    def add_new(self,item):
        if type(item) == Armor and not(item.isempty()):
            super().add_new(item)
        else:
            raise ValueError('expected Armor object, instead got ' + str(type(item)))

    def __eq__(self,tocompare):
        if type(tocompare) == Armors and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Armors object, instead got ' + str(type(tocompare)))


class Armor(Base_Equipment.Equip):
    damage_types = []

    def __eq__(self,tocompare):
        if type(tocompare) == Armor and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Armor object, instead got ' + str(type(tocompare)))

    def __init__(self,name,short_description=''):
        self.damage_types = []
        super().__init__(name,short_description)