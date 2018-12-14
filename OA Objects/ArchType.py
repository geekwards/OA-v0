import List_Object
import copy

class Archtypes:
    list_of_archtypes = []
    all_archtypes = []

    def add_new(self,archtype):
        self.all_archtypes.append(archtype)
        self.list_of_archtypes.append(List_Object.Listobject(archtype.name,archtype.short_description))

    def remove(self,archtype):
        self.list_of_archtypes.remove(self.get_list_item(self.all_archtypes.index(archtype)))
        self.all_archtypes.remove(archtype)

    def clone(self):
        return copy.copy(self)

    def equals(self,tocompare):
        same = True

        same = (len(self.get_all()) == len(tocompare.get_all()))

        if same:
            for idx,item in enumerate(tocompare.get_all()):
                same = same and item.equals(self.get_all()[idx])

        return same

    def isempty(self):
        return len(self.all_archtypes) == 0

    def get_all(self):
        return self.all_archtypes

    def get_list(self):
        return self.list_of_archtypes

    def get_list_item(self,idx):
        return self.list_of_archtypes[idx]

    def update(self,idx,archtype):
        if (idx == None) or (idx > len(self.all_archtypes)-1):
            self.add_new(archtype)
        else:
            self.all_archtypes[idx] = archtype
            self.list_of_archtypes[idx].name = archtype.name
            self.list_of_archtypes[idx].short_description = archtype.short_description

    def __getitem__(self,idx):
        if idx == None:
            return Archtype('','')
        else:
            return self.all_archtypes[idx]

    def __init__(self):
        self.all_archtypes = []
        self.list_of_archtypes = []

class Archtype:
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

    def isempty(self):
        return (self.name.strip() == '' and self.short_description.strip() == '')

    def clone(self):
        return copy.copy(self)

    def equals(self,tocompare):
        return ((self.name == tocompare.name)
            and (self.short_description == tocompare.short_description)
            and (self.description == tocompare.description)
            and (self.proficiency == tocompare.proficiency)
            and (self.str_bonus == tocompare.str_bonus)
            and (self.per_bonus == tocompare.per_bonus)
            and (self.int_bonus == tocompare.int_bonus)
            and (self.dex_bonus == tocompare.dex_bonus)
            and (self.cha_bonus == tocompare.cha_bonus)
            and (self.vit_bonus == tocompare.vit_bonus)
            and (self.mag_bonus == tocompare.mag_bonus)
            and (self.stamina_bonus == tocompare.stamina_bonus)
            and (self.attack_bonus == tocompare.attack_bonus)
            and (self.reflex_bonus == tocompare.reflex_bonus)
            and (self.feats == tocompare.feats)
            and (self.movement == tocompare.movement)
            and (self.skill_points == tocompare.skill_points)
            and (self.level_health == tocompare.level_health)
            )

    def __init__(self,name,short_description):
        self.name = name
        self.short_description = short_description
