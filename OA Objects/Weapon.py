import Base_Object

class Weapons(Base_Object.Set_of_Items):
    pass

class Weapon(Base_Object.Item):
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
