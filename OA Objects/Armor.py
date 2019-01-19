import Base_Equipment

class Armors(Base_Equipment.Base_equipment):
    pass

class Armor(Base_Equipment.Equip):
    damage_types = []

    def __init__(self,name,short_description=''):
        self.damage_types = []
        super().__init__(name,short_description)