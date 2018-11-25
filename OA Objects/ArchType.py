import ListObject

class Archtypes:
    listOfArchtypes = []
    archtypes = []

    def AddNew(current,archType):
        current.archtypes.append(archType)
        current.listOfArchtypes.append(ListObject.Listobject(archType.name,archType.shortDescription))

    def GetList(current):
        return current.listOfArchtypes

    def __getitem__(current,idx):
        return current.archtypes[idx]

    def __init__(self):
        self.archtypes = []

class Archtype:
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
