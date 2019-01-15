import Base_Equipment

class Weapons(Base_Equipment.Base_equipment):
    pass

class Weapon(Base_Equipment.Equip):
    hands = 0
    weapon_type = ''
    range = 0
    ammo_type = ''
    damage_types = []
