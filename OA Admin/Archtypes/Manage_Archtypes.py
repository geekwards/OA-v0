from Tkinter import *

import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import GUI_List
import GUI_Archtype
import Arch_Type

def save_archtype(archtype):
    global current_set

    current_set.update(archtype)

    save_archtypes()

def save_archtypes():
    global current_set

    data = ET.Element('archtypes')

    for item in current_set:
        arch = ET.SubElement(data, 'archtype')
        ET.SubElement(arch, 'name').text = item.name
        ET.SubElement(arch, 'shortDescription').text = item.short_description
        ET.SubElement(arch, 'description').text = item.description
        ET.SubElement(arch, 'proficiency').text = item.proficiency
        ET.SubElement(arch, 'strBonus').text = item.str_bonus
        ET.SubElement(arch, 'perBonus').text = item.per_bonus
        ET.SubElement(arch, 'intBonus').text = item.int_bonus
        ET.SubElement(arch, 'dexBonus').text = item.dex_bonus
        ET.SubElement(arch, 'chaBonus').text = item.cha_bonus
        ET.SubElement(arch, 'vitBonus').text = item.vit_bonus
        ET.SubElement(arch, 'magBonus').text = item.mag_bonus
        ET.SubElement(arch, 'staminaBonus').text = item.stamina_bonus
        ET.SubElement(arch, 'attackBonus').text = item.attack_bonus
        ET.SubElement(arch, 'reflexBonus').text = item.reflex_bonus
        ET.SubElement(arch, 'feats').text = item.feats
        ET.SubElement(arch, 'movement').text = item.movement
        ET.SubElement(arch, 'skillPoints').text = item.skill_points
        ET.SubElement(arch, 'levelHealth').text = item.level_health

    filename = app_config.filepath + app_config.filename
    backup_filename = app_config.backup_filepath + app_config.backup_filename

    copy2(filename, backup_filename)
    open(filename, 'w').write(ET.tostring(data))

    GUI_List.build_list("ArchTypes", current_set.get_list(), edit_archtype, remove_archtype)

def remove_archtype(idx):
    global current_set

    current_set.remove(current_set[idx])

    save_archtypes()

def edit_archtype(top, idx):
    global current_set
    global edit_window

    edit_window = None

    if edit_window == None or not Toplevel.winfo_exists(edit_window):
        edit_window, top = GUI_Archtype.create_toplevel1(top)

    if idx == None:
        GUI_Archtype.load_form(Arch_Type.Archtype('',''), save_archtype)
    else:
        GUI_Archtype.load_form(current_set[idx], save_archtype)

    edit_window.mainloop()

def archtype_list():
    global current_set
    global list_window

    list_window, top = GUI_List.create_toplevel1(None)

    GUI_List.build_list("ArchTypes", current_set.get_list(), edit_archtype, remove_archtype)

    list_window.mainloop()

def load_archtypes():
    global current_set

    current_set = Arch_Type.Archtypes()

    filename = app_config.filepath + app_config.filename
    tree = ET.parse(filename)

    data_root = tree.getroot()

    for archtype in data_root:
        current_archtype = Arch_Type.Archtype(archtype.find('name').text, archtype.find('shortDescription').text)
        current_archtype.description = archtype.find('description').text
        current_archtype.proficiency = archtype.find('proficiency').text
        current_archtype.str_bonus = archtype.find('strBonus').text
        current_archtype.per_bonus = archtype.find('perBonus').text
        current_archtype.int_bonus = archtype.find('intBonus').text
        current_archtype.dex_bonus = archtype.find('dexBonus').text
        current_archtype.cha_bonus = archtype.find('chaBonus').text
        current_archtype.vit_bonus = archtype.find('vitBonus').text
        current_archtype.mag_bonus = archtype.find('magBonus').text
        current_archtype.stamina_bonus = archtype.find('staminaBonus').text
        current_archtype.attack_bonus = archtype.find('attackBonus').text
        current_archtype.reflex_bonus = archtype.find('reflexBonus').text
        current_archtype.feats = archtype.find('feats').text
        current_archtype.movement = archtype.find('movement').text
        current_archtype.skill_points = archtype.find('skillPoints').text
        current_archtype.level_health = archtype.find('levelHealth').text

        current_set.add_new(current_archtype)

if __name__ == '__main__':

    load_archtypes()

    archtype_list()
