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
backup_filename = "C:\Projects\OA Manager v0\OA Data Files\Archtypes" + strftime("%Y%m%d%H%M%S", gmtime()) + ".dat"

def save_archtype(archtype):
    global current_set
    global filename

    current_set.update(archtype)

    data = ET.Element('archtypes')

    for item in current_set:
        arch = ET.SubElement(data, 'archtype')
        ET.SubElement(arch, 'name').text = item.name
        ET.SubElement(arch, 'shortDescription').text = item.shortDescription
        ET.SubElement(arch, 'description').text = item.description
        ET.SubElement(arch, 'proficiency').text = item.proficiency
        ET.SubElement(arch, 'strBonus').text = item.strBonus
        ET.SubElement(arch, 'perBonus').text = item.perBonus
        ET.SubElement(arch, 'intBonus').text = item.intBonus
        ET.SubElement(arch, 'dexBonus').text = item.dexBonus
        ET.SubElement(arch, 'chaBonus').text = item.chaBonus
        ET.SubElement(arch, 'vitBonus').text = item.vitBonus
        ET.SubElement(arch, 'magBonus').text = item.magBonus
        ET.SubElement(arch, 'staminaBonus').text = item.staminaBonus
        ET.SubElement(arch, 'attackBonus').text = item.attackBonus
        ET.SubElement(arch, 'reflexBonus').text = item.reflexBonus
        ET.SubElement(arch, 'feats').text = item.feats
        ET.SubElement(arch, 'movement').text = item.movement
        ET.SubElement(arch, 'skillPoints').text = item.skillPoints
        ET.SubElement(arch, 'levelHealth').text = item.levelHealth

    copy2(filename, backup_filename)
    open(filename, 'w').write(ET.tostring(data))

def edit_archtype(top, idx):
    global current_set
    global edit_window

    edit_window = None

    if edit_window == None or not Toplevel.winfo_exists(edit_window):
        edit_window, top = GUI_Archtype.create_toplevel1(top)

    GUI_Archtype.load_form(current_set[idx], save_archtype)

    edit_window.mainloop()

def archtype_list():
    global current_set

    root, top = GUI_List.create_root()

    GUI_List.build_list("ArchTypes", current_set.get_list(), edit_archtype)

    root.mainloop()

def load_archtypes():
    global current_set
    global filename
    global current_archtype

    current_set = ArchType.Archtypes()

    tree = ET.parse(filename)

    data_root = tree.getroot()

    for archtype in data_root:
        current_archtype = ArchType.Archtype(archtype.find('name').text, archtype.find('shortDescription').text)
        current_archtype.description = archtype.find('description').text
        current_archtype.proficiency = archtype.find('proficiency').text
        current_archtype.strBonus = archtype.find('strBonus').text
        current_archtype.perBonus = archtype.find('perBonus').text
        current_archtype.intBonus = archtype.find('intBonus').text
        current_archtype.dexBonus = archtype.find('dexBonus').text
        current_archtype.chaBonus = archtype.find('chaBonus').text
        current_archtype.vitBonus = archtype.find('vitBonus').text
        current_archtype.magBonus = archtype.find('magBonus').text
        current_archtype.staminaBonus = archtype.find('staminaBonus').text
        current_archtype.attackBonus = archtype.find('attackBonus').text
        current_archtype.reflexBonus = archtype.find('reflexBonus').text
        current_archtype.feats = archtype.find('feats').text
        current_archtype.movement = archtype.find('movement').text
        current_archtype.skillPoints = archtype.find('skillPoints').text
        current_archtype.levelHealth = archtype.find('levelHealth').text

        current_set.add_new(current_archtype)

if __name__ == '__main__':
    global myset

    myset = ArchType.Archtypes()

    load_archtypes()

    archtype_list()
