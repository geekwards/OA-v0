import List_Object
import copy

class Races:
    list_of_races = []
    all_races = []

    def add_new(self,race):
        self.all_races.append(race)
        self.list_of_races.append(List_Object.List_object(race.name,race.short_description))

    def remove(self,race):
        self.list_of_races.remove(self.list_of_races[self.all_races.index(race)])
        self.all_races.remove(self.get_race(race.name))

    def equals(self,tocompare):
        same = (len(self.all_races) == len(tocompare.all_races))
        if same:
            for idx,item in enumerate(tocompare.all_races):
                same = same and item.equals(self.all_races[idx])

        return same

    def clone(self):
        return copy.deepcopy(self)

    def isempty(self):
        return len(self.all_races) == 0

    def update(self,race):
        found = False
        for item in self.all_races:
            if item.name == race.name:
                idx = self.all_races.index(item)
                self.all_races[idx] = race
                self.list_of_races[idx].name = race.name
                self.list_of_races[idx].short_description = race.short_description
                found = True
                break

        if not found:
            self.add_new(race)

    def get_race(self,name):
        for item in self.all_races:
            if item.name == name:
                return item

        return Race('','')

    def __len__(self):
        return len(self.all_races)

    def __init__(self):
        self.all_races = []
        self.list_of_races = []

class Race:
    name = ''
    short_description = ''
    description = ''
    size = ''
    body = ''
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
    languages_bonus = []

    def equals(self,tocompare):
        return ((self.name == tocompare.name)
            and (self.short_description == tocompare.short_description)
            and (self.description == tocompare.description)
            and (self.size == tocompare.size)
            and (self.body == tocompare.body)
            and (self.foci == tocompare.foci)
            and (self.feats == tocompare.feats)
            and (self.str_bonus == tocompare.str_bonus)
            and (self.per_bonus == tocompare.per_bonus)
            and (self.int_bonus == tocompare.int_bonus)
            and (self.dex_bonus == tocompare.dex_bonus)
            and (self.cha_bonus == tocompare.cha_bonus)
            and (self.vit_bonus == tocompare.vit_bonus)
            and (self.mag_bonus == tocompare.mag_bonus)
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
        self.foci = []
        self.feats = []
        self.languages_bonus = []

