import ListObject
import copy

class Archtypes:
    listOfArchtypes = []
    archtypes = []

    def AddNew(current,archtype):
        current.archtypes.append(archtype)
        current.listOfArchtypes.append(ListObject.Listobject(archtype.name,archtype.shortDescription))

    def GetList(current):
        return current.listOfArchtypes

    def Clone(current):
        return copy.copy(current)

    def Update(current,archtype):

        found = False

        for idx, at in enumerate(current.archtypes):
            if at.name == archtype.name:
                found = True
                current.archtypes[idx] = archtype

        if found:
            for idx, lo in enumerate(current.listOfArchtypes):
                if lo.name == archtype.name:
                    current.listOfArchtypes[idx].shortDescription = archtype.shortDescription
        else:
            current.AddNew(archtype)

    def __getitem__(current,idx):
        return current.archtypes[idx]

    def __init__(self):
        self.archtypes = []

class Archtype:
    description = ""
    proficiency = ""
    strBonus = 0
    perBonus = 0
    intBonus = 0
    dexBonus = 0
    chaBonus = 0
    vitBonus = 0
    magBonus = 0
    staminaBonus = 0
    attackBonus = 0
    reflexBonus = 0
    feats = 0
    movement = 0
    skillPoints = 0
    levelHealth = ""

    def Clone(current):
        return copy.copy(current)

    def __init__(self, name, shortDescr):
        self.name = name
        self.shortDescription = shortDescr
