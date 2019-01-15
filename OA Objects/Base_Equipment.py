import Base_Object

class Base_equipment(Base_Object.Set_of_Items):
    pass

class Equip(Base_Object.Item):
    name = ''
    short_description = ''
    description = ''
    value = 0
    weight = 0
    health = 0
    capacity = 0
    special = ''
