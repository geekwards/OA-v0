import Base_Equipment

class Foods(Base_Equipment.Base_equipment):
    def add_new(self,item):
        if type(item) == Food and not(item.isempty()):
            super().add_new(item)
        else:
            raise ValueError('expected Food object, instead got ' + str(type(item)))

    def __eq__(self,tocompare):
        if type(tocompare) == Foods and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Foods object, instead got ' + str(type(tocompare)))

class Food(Base_Equipment.Equip):
    def __eq__(self,tocompare):
        if type(tocompare) == Food and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Food object, instead got ' + str(type(tocompare)))