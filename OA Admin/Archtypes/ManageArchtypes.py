from Tkinter import *

import sys, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA GUI'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Objects'))

import GUI_List
import GUI_Archtype
import ArchType

def EditArchtype(top, idx):
    global mySet

    editRoot, top = GUI_Archtype.create_Toplevel1(top)

    GUI_Archtype.loadForm(mySet[idx])

    editRoot.mainloop()

def ArchtypeList():
    global mySet

    root, top = GUI_List.create_Root()

    GUI_List.buildList("ArchTypes", mySet.GetList(), EditArchtype)

    root.mainloop()

def LoadArchtypes():
    global mySet

    mySet.AddNew(ArchType.Archtype("TestArch", "TestDesc"))
    mySet[0].description = "Description12"
    mySet[0].proficiency = "TestProf"
    mySet[0].strBonus = 1
    mySet[0].perBonus = 2
    mySet[0].intBonus = 3
    mySet[0].dexBonus = -1
    mySet[0].chaBonus = -2
    mySet[0].vitBonus = -3
    mySet[0].magBonus = -5
    mySet[0].staminaBonus = 5
    mySet[0].attackBonus = 2
    mySet[0].reflexBonus = 1
    mySet[0].feats = []
    mySet[0].movement = 8
    mySet[0].skillPoints = 12
    mySet[0].levelHealth = "more health"
    mySet.AddNew(ArchType.Archtype("TestArch2", "TestDesc2"))
    mySet[1].description = "Description34"
    mySet[1].proficiency = "TestProf2"
    mySet[1].strBonus = 1
    mySet[1].perBonus = 2
    mySet[1].intBonus = 3
    mySet[1].dexBonus = -1
    mySet[1].chaBonus = -2
    mySet[1].vitBonus = -3
    mySet[1].magBonus = -5
    mySet[1].staminaBonus = 5
    mySet[1].attackBonus = 2
    mySet[1].reflexBonus = 1
    mySet[1].feats = []
    mySet[1].movement = 8
    mySet[1].skillPoints = 12
    mySet[1].levelHealth = "less health"

if __name__ == '__main__':
    global mySet

    mySet = ArchType.Archtypes()

    LoadArchtypes()

    ArchtypeList()
