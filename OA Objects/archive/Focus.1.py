import List_Object
import copy

class Foci:
    list_of_foci = []
    all_foci = []

    def add_new(self,focus):
        self.all_foci.append(focus)
        self.list_of_foci.append(List_Object.List_object(focus.name,focus.short_description))

    def remove(self,focus):
        self.list_of_foci.remove(self.list_of_foci[self.all_foci.index(focus)])
        self.all_foci.remove(self.get_race(focus.name))

    def equals(self,tocompare):
        same = (len(self.all_foci) == len(tocompare.all_foci))
        if same:
            for idx,item in enumerate(tocompare.all_foci):
                same = same and item.equals(self.all_foci[idx])

        return same

    def clone(self):
        return copy.deepcopy(self)

    def isempty(self):
        return len(self.all_foci) == 0

    def update(self,focus):
        found = False
        for item in self.all_foci:
            if item.name == focus.name:
                idx = self.all_foci.index(item)
                self.all_foci[idx] = focus
                self.list_of_foci[idx].name = focus.name
                self.list_of_foci[idx].short_description = focus.short_description
                found = True
                break

        if not found:
            self.add_new(focus)

    def get_focus(self,name):
        for item in self.all_foci:
            if item.name == name:
                return item

        return Focus('','')

    def __len__(self):
        return len(self.all_foci)

    def __init__(self):
        self.all_foci = []
        self.list_of_foci = []

class Focus:
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

    def equals(self,tocompare):
        return ((self.name == tocompare.name)
            and (self.short_description == tocompare.short_description)
            and (self.description == tocompare.description)
            and (self.str_bonus == tocompare.str_bonus)
            and (self.per_bonus == tocompare.per_bonus)
            and (self.int_bonus == tocompare.int_bonus)
            and (self.dex_bonus == tocompare.dex_bonus)
            and (self.cha_bonus == tocompare.cha_bonus)
            and (self.vit_bonus == tocompare.vit_bonus)
            and (self.mag_bonus == tocompare.mag_bonus)
            and (self.str_skill_bonus == tocompare.str_skill_bonus)
            and (self.per_skill_bonus == tocompare.per_skill_bonus)
            and (self.int_skill_bonus == tocompare.int_skill_bonus)
            and (self.dex_skill_bonus == tocompare.dex_skill_bonus)
            and (self.cha_skill_bonus == tocompare.cha_skill_bonus)
            and (self.vit_skill_bonus == tocompare.vit_skill_bonus)
            and (self.mag_skill_bonus == tocompare.mag_skill_bonus)
            and (self.will_bonus == tocompare.will_bonus)
            and (self.fortitude_bonus == tocompare.fortitude_bonus)
            and (self.reflex_bonus == tocompare.reflex_bonus)
            and (self.languages_bonus == tocompare.languages_bonus)
            )

    def clone(self):
        return copy.deepcopy(self)

    def isempty(self):
        return (self.name.strip() == '')

    def __init__(self,name,short_descr=''):
        self.name = name
        self.short_description = short_descr
        self.languages_bonus = []

