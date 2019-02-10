import Base_Object

class Foci(Base_Object.Set_of_Items):
    def add_new(self,item):
        if type(item) == Focus and not(item.isempty()):
            super().add_new(item)
        else:
            raise ValueError('expected Focus object, instead got ' + str(type(item)))

    def __eq__(self,tocompare):
        if type(tocompare) == Foci and not(tocompare.isempty()):
            return super().__eq__(tocompare)
        else:
            raise ValueError('expected Foci object, instead got ' + str(type(tocompare)))

class Focus(Base_Object.Item):
    name = ''
    short_description = ''
    description = ''
    str_bonus = 0
    per_bonus = 0
    int_bonus = 0
    dex_bonus = 0
    cha_bonus = 0
    vit_bonus = 0
    mag_bonus = 0
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
        if type(tocompare) == Focus and not(tocompare.isempty()):
            same = (self.name == tocompare.name)
            same = same and (self.short_description == tocompare.short_description)
            same = same and (self.description == tocompare.description)
            same = same and (self.str_bonus == tocompare.str_bonus)
            same = same and (self.per_bonus == tocompare.per_bonus)
            same = same and (self.int_bonus == tocompare.int_bonus)
            same = same and (self.dex_bonus == tocompare.dex_bonus)
            same = same and (self.cha_bonus == tocompare.cha_bonus)
            same = same and (self.vit_bonus == tocompare.vit_bonus)
            same = same and (self.mag_bonus == tocompare.mag_bonus)
            same = same and (self.str_skill_bonus == tocompare.str_skill_bonus)
            same = same and (self.per_skill_bonus == tocompare.per_skill_bonus)
            same = same and (self.int_skill_bonus == tocompare.int_skill_bonus)
            same = same and (self.dex_skill_bonus == tocompare.dex_skill_bonus)
            same = same and (self.cha_skill_bonus == tocompare.cha_skill_bonus)
            same = same and (self.vit_skill_bonus == tocompare.vit_skill_bonus)
            same = same and (self.mag_skill_bonus == tocompare.mag_skill_bonus)
            same = same and (self.will_bonus == tocompare.will_bonus)
            same = same and (self.fortitude_bonus == tocompare.fortitude_bonus)
            same = same and (self.reflex_bonus == tocompare.reflex_bonus)
            same = same and (len(self.languages_bonus)==len(tocompare.languages_bonus))
            if same and len(self.languages_bonus)>0:
                for idx,lang in enumerate(self.languages_bonus):
                    same = same and (lang.name == tocompare.languages_bonus[idx].name and lang.short_description == tocompare.languages_bonus[idx].short_description)
            return same
        else:
            raise ValueError('expected Focus object, instead got ' + str(type(tocompare)))

    def __init__(self,name,short_description=''):
        self.languages_bonus = []
        super().__init__(name,short_description)