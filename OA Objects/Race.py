import Base_Object

class Races(Base_Object.Set_of_Items):
    def add_new(self,item):
        if type(item) == Race and not(item.isempty()):
            super().add_new(item)
        else:
            raise ValueError('expected Race object, instead got ' + str(type(item)))

    def __eq__(self,tocompare):
        if type(tocompare) == Races and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Races object, instead got ' + str(type(tocompare)))

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

    def __eq__(self,tocompare):
        if type(tocompare) == Race and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Race object, instead got ' + str(type(tocompare)))

    def __init__(self,name,short_description=''):
        self.foci=[]
        self.feats=[]
        self.languages_bonus=[]
        super().__init__(name,short_description)