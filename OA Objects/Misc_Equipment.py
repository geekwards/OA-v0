import Base_Equipment

class Misc_equipment(Base_Equipment.Base_equipment):
    def add_new(self,item):
        if type(item) == Misc_equip and not(item.isempty()):
            super().add_new(item)
        else:
            raise ValueError('expected Misc_equip object, instead got ' + str(type(item)))

    def __eq__(self,tocompare):
        if type(tocompare) == Misc_equipment and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Misc_equipment object, instead got ' + str(type(tocompare)))

class Misc_equip(Base_Equipment.Equip):
    def __eq__(self,tocompare):
        if type(tocompare) == Misc_equip and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Misc_equip object, instead got ' + str(type(tocompare)))