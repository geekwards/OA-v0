import Base_Object

class Archtypes(Base_Object.Set_of_Items):
    def add_new(self,item):
        if type(item) == Archtype and not(item.isempty()):
            super().add_new(item)
        else:
            raise ValueError('expected Archtype object, instead got ' + str(type(item)))

    def __eq__(self,tocompare):
        if type(tocompare) == Archtypes and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Archtypes object, instead got ' + str(type(tocompare)))

class Archtype(Base_Object.Item):
    name = ''
    short_description = ''
    description = ''
    proficiency = ''
    str_bonus = 0
    per_bonus = 0
    int_bonus = 0
    dex_bonus = 0
    cha_bonus = 0
    vit_bonus = 0
    mag_bonus = 0
    stamina_bonus = 0
    attack_bonus = 0
    reflex_bonus = 0
    feats = 0
    movement = 0
    skill_points = 0
    level_health = ''

    def __eq__(self,tocompare):
        if type(tocompare) == Archtype and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Archtype object, instead got ' + str(type(tocompare)))