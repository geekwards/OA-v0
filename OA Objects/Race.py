import List_Object
import copy

class Races:
    list_of_races = []
    all_races = []

    def add_new(self,race):
        self.all_races.append(race)
        self.list_of_races.append(List_Object.Listobject(race.name,race.short_description))

    def remove(self,race):
        self.list_of_races.remove(self.get_list_item(self.all_races.index(race)))
        self.all_races.remove(race)

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
        return len(self.all_races) == 0

    def get_all(self):
        return self.all_races

    def get_list(self):
        return self.list_of_races

    def get_list_item(self,idx):
        return self.list_of_races[idx]

    def update(self,idx,race):
        if (idx == None) or (idx > len(self.all_races)-1):
            self.add_new(race)
        else:
            self.all_races[idx] = race
            self.list_of_races[idx].name = race.name

    def __getitem__(self,idx):
        if idx == None:
            return Race('')
        else:
            return self.all_races[idx]

    def __init__(self):
        self.all_races = []
        self.list_of_races = []

class Race:
    description = ''
    size = ''
    body_type = ''
    foci = []
    feats = []
    str_bonus = 0
    per_bonus = 0
    int_bonus = 0
    dex_bonus = 0
    cha_bonus = 0
    vit_bonus = 0
    mag_bonus = 0
    will_bonus = 0
    fortitude_bonus = 0
    reflex_bonus = 0
    language_bonuses = []

    def isempty(self):
        return (self.name.strip() == '')

    def clone(self):
        return copy.copy(self)

    def equals(self,tocompare):
        return ((self.name == tocompare.name)
            and (self.description == tocompare.description)
            and (self.size == tocompare.size)
            and (self.body_type == tocompare.body_type)
            and (self.foci == tocompare.foci)
            and (self.feats == tocompare.feats)
            and (self.str_bonus == tocompare.str_bonus)
            and (self.per_bonus == tocompare.per_bonus)
            and (self.body_type == tocompare.body_type)
            and (self.int_bonus == tocompare.int_bonus)
            and (self.dex_bonus == tocompare.dex_bonus)
            and (self.cha_bonus == tocompare.cha_bonus)
            and (self.vit_bonus == tocompare.vit_bonus)
            and (self.mag_bonus == tocompare.mag_bonus)
            and (self.will_bonus == tocompare.will_bonus)
            and (self.fortitude_bonus == tocompare.fortitude_bonus)
            and (self.reflex_bonus == tocompare.reflex_bonus)
            and (self.language_bonuses == tocompare.language_bonuses)
            )

    def __init__(self,name):
        self.name = name
