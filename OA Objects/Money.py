import Base_Equipment

class Monies(Base_Equipment.Base_equipment):
    def add_new(self,item):
        if type(item) == Money and not(item.isempty()):
            super().add_new(item)
        else:
            raise ValueError('expected Money object, instead got ' + str(type(item)))

    def __eq__(self,tocompare):
        if type(tocompare) == Monies and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Monies object, instead got ' + str(type(tocompare)))

class Money(Base_Equipment.Equip):
    def __eq__(self,tocompare):
        if type(tocompare) == Money and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Money object, instead got ' + str(type(tocompare)))
