import List_Object
import copy

class Archtypes:
    list_of_archtypes = []
    all_archtypes = []

    def add_new(current,archtype):
        current.all_archtypes.append(archtype)
        current.list_of_archtypes.append(List_Object.Listobject(archtype.name,archtype.short_description))

    def remove(current,archtype):
        current.list_of_archtypes.remove(current.get_list_item(current.all_archtypes.index(archtype)))
        current.all_archtypes.remove(archtype)

    def get_all(current):
        return current.all_archtypes

    def get_list(current):
        return current.list_of_archtypes

    def get_list_item(current,idx):
        return current.list_of_archtypes[idx]

    def update(current,idx,archtype):
        if idx == None:
            current.add_new(archtype)
        else:
            current.all_archtypes[idx] = archtype
            current.list_of_archtypes[idx].short_description = archtype.short_description

    def __getitem__(current,idx):
        if idx == None:
            return Archtype('','')
        else:
            return current.all_archtypes[idx]

    def __init__(self):
        self.all_archtypes = []

class Archtype:
    description = ""
    proficiency = ""
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
    level_health = ""

    def isempty(current):
        return (current.name == '' and current.short_description == '')

    def clone(current):
        return copy.copy(current)

    def __init__(self, name, short_description):
        self.name = name
        self.short_description = short_description
