import Base_Object

class Containers(Base_Object.Set_of_Items):
    pass

class Container(Base_Object.Item):
    name = ''
    short_description = ''
    description = ''
    value = 0
    weight = 0
    health = 0
    capacity = 0
    special = ''

