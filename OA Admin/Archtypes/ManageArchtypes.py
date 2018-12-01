from Tkinter import *

import sys, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA GUI'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Objects'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files'))

import GUI_List
import GUI_Archtype
import ArchType
import xml.etree.ElementTree as ET

def SaveArchtype(archtype):
    global mySet

    mySet.Update(archtype)

    # data = ET.Element('archtypes')
    #
    # for at
    #
    # arch = ET.SubElement(data, 'archtype')


def EditArchtype(top, idx):
    global mySet
    global editWindow

    if editWindow == None or not Toplevel.winfo_exists(editWindow):
        editWindow, top = GUI_Archtype.create_Toplevel1(top)

    GUI_Archtype.loadForm(mySet[idx], SaveArchtype)

    editWindow.mainloop()

def ArchtypeList():
    global mySet
    global editWindow

    editWindow = None

    root, top = GUI_List.create_Root()

    GUI_List.buildList("ArchTypes", mySet.GetList(), EditArchtype)

    root.mainloop()

def LoadArchtypes():
    global mySet

    mySet = ArchType.Archtypes()

    tree = ET.parse("C:\Projects\OA Manager v0\OA Data Files\Archtypes.dat")

    dataRoot = tree.getroot()

    for archtype in dataRoot:
        currArchType = ArchType.Archtype(archtype.find('name').text, archtype.find('shortdesc').text)
        currArchType.description = archtype.find('description').text
        currArchType.proficiency = archtype.find('proficiency').text
        currArchType.strBonus = archtype.find('strBonus').text
        currArchType.perBonus = archtype.find('perBonus').text
        currArchType.intBonus = archtype.find('intBonus').text
        currArchType.dexBonus = archtype.find('dexBonus').text
        currArchType.chaBonus = archtype.find('chaBonus').text
        currArchType.vitBonus = archtype.find('vitBonus').text
        currArchType.magBonus = archtype.find('magBonus').text
        currArchType.staminaBonus = archtype.find('staminaBonus').text
        currArchType.attackBonus = archtype.find('attackBonus').text
        currArchType.reflexBonus = archtype.find('reflexBonus').text
        currArchType.feats = archtype.find('feats').text
        currArchType.movement = archtype.find('movement').text
        currArchType.skillPoints = archtype.find('skillPoints').text
        currArchType.levelHealth = archtype.find('levelHealth').text

        mySet.AddNew(currArchType)

if __name__ == '__main__':
    global mySet

    mySet = ArchType.Archtypes()

    LoadArchtypes()

    ArchtypeList()
