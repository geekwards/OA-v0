import ListObject

class Archtypes:
    listOfArchtypes = []
    archtypes = []

    def AddNew(current,archtype):
        current.archtypes.append(archtype)
        current.listOfArchtypes.append(ListObject.Listobject(archtype.name,archtype.shortDescription))

    def GetList(current):
        return current.listOfArchtypes

    def Update(current,archtype):
        for idx, at in enumerate(current.archtypes):
            if at.name == archtype.name:
                current.archtypes[idx] = archtype

        for idx, lo in enumerate(current.listOfArchtypes):
            if lo.name == archtype.name:
                current.listOfArchtypes[idx].shortDescription = archtype.shortDescription

        for temp in current.archtypes:
            print temp.name
            print temp.shortDescription

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

    def __init__(self, name, shortDescr):
        self.name = name
        self.shortDescription = shortDescr
