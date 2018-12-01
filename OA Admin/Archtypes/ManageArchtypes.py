from Tkinter import *

import sys, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA GUI'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Objects'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files'))

import GUI_List
import GUI_Archtype
import ArchType
import xml.etree.ElementTree as ET
from time import gmtime, strftime
from shutil import copy2

filename = "C:\Projects\OA Manager v0\OA Data Files\Archtypes.dat"
backupFilename = "C:\Projects\OA Manager v0\OA Data Files\Archtypes" + strftime("%Y%m%d%H%M%S", gmtime()) + ".dat"

def SaveArchtype(archtype):
    global mySet
    global filename

    mySet.Update(archtype)

    data = ET.Element('archtypes')

    for at in mySet:
        arch = ET.SubElement(data, 'archtype')
        ET.SubElement(arch, 'name').text = at.name
        ET.SubElement(arch, 'shortDescription').text = at.shortDescription
        ET.SubElement(arch, 'description').text = at.description
        ET.SubElement(arch, 'proficiency').text = at.proficiency
        ET.SubElement(arch, 'strBonus').text = at.strBonus
        ET.SubElement(arch, 'perBonus').text = at.perBonus
        ET.SubElement(arch, 'intBonus').text = at.intBonus
        ET.SubElement(arch, 'dexBonus').text = at.dexBonus
        ET.SubElement(arch, 'chaBonus').text = at.chaBonus
        ET.SubElement(arch, 'vitBonus').text = at.vitBonus
        ET.SubElement(arch, 'magBonus').text = at.magBonus
        ET.SubElement(arch, 'staminaBonus').text = at.staminaBonus
        ET.SubElement(arch, 'attackBonus').text = at.attackBonus
        ET.SubElement(arch, 'reflexBonus').text = at.reflexBonus
        ET.SubElement(arch, 'feats').text = at.feats
        ET.SubElement(arch, 'movement').text = at.movement
        ET.SubElement(arch, 'skillPoints').text = at.skillPoints
        ET.SubElement(arch, 'levelHealth').text = at.levelHealth

    copy2(filename, backupFilename)
    open(filename, 'w').write(ET.tostring(data))

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
    global filename

    mySet = ArchType.Archtypes()

    tree = ET.parse(filename)

    dataRoot = tree.getroot()

    for archtype in dataRoot:
        currArchType = ArchType.Archtype(archtype.find('name').text, archtype.find('shortDescription').text)
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
