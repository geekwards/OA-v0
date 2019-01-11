import Base_Object

class Races(Base_Object.Set_of_Items):
    pass

class Race(Base_Object.Item):
    name = ''
    short_description = ''
    description = ''
    size = ''
    body = ''
    foci = []
    feats = []
    str_skill_bonus = 0
    per_skill_bonus = 0
    int_skill_bonus = 0
    dex_skill_bonus = 0
    cha_skill_bonus = 0
    vit_skill_bonus = 0
    mag_skill_bonus = 0
    will_bonus = 0
    fortitude_bonus = 0
    reflex_bonus = 0
    languages_bonus = []
