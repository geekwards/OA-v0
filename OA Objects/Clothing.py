import Base_Equipment

class Clothing(Base_Equipment.Base_equipment):
    def add_new(self,item):
        if type(item) == Garment and not(item.isempty()):
            super().add_new(item)
        else:
            raise ValueError('expected Garment object, instead got ' + str(type(item)))

    def __eq__(self,tocompare):
        if type(tocompare) == Clothing and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Clothing object, instead got ' + str(type(tocompare)))

class Garment(Base_Equipment.Equip):

    def __eq__(self,tocompare):
        if type(tocompare) == Garment and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Garment object, instead got ' + str(type(tocompare)))
