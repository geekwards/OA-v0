import Base_Equipment

class Containers(Base_Equipment.Base_equipment):
    def add_new(self,item):
        if type(item) == Container and not(item.isempty()):
            super().add_new(item)
        else:
            raise ValueError('expected Container object, instead got ' + str(type(item)))

    def __eq__(self,tocompare):
        if type(tocompare) == Containers and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Containers object, instead got ' + str(type(tocompare)))

class Container(Base_Equipment.Equip):
    def __eq__(self,tocompare):
        if type(tocompare) == Container and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Container object, instead got ' + str(type(tocompare)))

