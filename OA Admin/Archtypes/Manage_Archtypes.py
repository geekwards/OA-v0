import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import GUI_List
import GUI_Archtype
import Archtype

def save_archtype(idx,archtype):
    global current_set

    current_set.update(idx,archtype)
    GUI_List.build_list("ArchTypes",current_set.get_list(),edit_archtype, remove_archtype)

def save_archtypes(filename=None,backup_filename=None):
    global current_set

    data=ET.Element('archtypes')
    for item in current_set:
        arch=ET.SubElement(data,'archtype')
        ET.SubElement(arch,'name').text = item.name
        ET.SubElement(arch,'shortDescription').text = item.short_description
        ET.SubElement(arch,'description').text = item.description
        ET.SubElement(arch,'proficiency').text = item.proficiency
        ET.SubElement(arch,'strBonus').text = item.str_bonus
        ET.SubElement(arch,'perBonus').text = item.per_bonus
        ET.SubElement(arch,'intBonus').text = item.int_bonus
        ET.SubElement(arch,'dexBonus').text = item.dex_bonus
        ET.SubElement(arch,'chaBonus').text = item.cha_bonus
        ET.SubElement(arch,'vitBonus').text = item.vit_bonus
        ET.SubElement(arch,'magBonus').text = item.mag_bonus
        ET.SubElement(arch,'staminaBonus').text = item.stamina_bonus
        ET.SubElement(arch,'attackBonus').text = item.attack_bonus
        ET.SubElement(arch,'reflexBonus').text = item.reflex_bonus
        ET.SubElement(arch,'feats').text = item.feats
        ET.SubElement(arch,'movement').text = item.movement
        ET.SubElement(arch,'skillPoints').text = item.skill_points
        ET.SubElement(arch,'levelHealth').text = item.level_health

    if filename == None:
        filename = app_config.file_path + app_config.filename
    if backup_filename == None:
        backup_filename = app_config.backup_file_path + app_config.backup_filename

    copy2(filename,backup_filename)
    open(filename,'w').write(ET.tostring(data))

def remove_archtype(idx):
    global current_set

    current_set.remove(current_set[idx])

def edit_archtype(parent,idx):
    global current_set
    global archtype_window

    archtype_window = None

    if archtype_window == None or not Toplevel.winfo_exists(archtype_window):
        archtype_window,archtype_form = GUI_Archtype.create_archtype_form(parent)

    GUI_Archtype.load_data(current_set[idx],save_archtype, idx)
    archtype_window.mainloop()

def archtype_list():
    global current_set
    global loaded_set
    global list_window

    list_window,list_form = GUI_List.create_list_form(None)

    GUI_List.build_list("ArchTypes",current_set.get_list(),edit_archtype,remove_archtype)
    list_window.mainloop()

    if not current_set.equals(loaded_set):
        save_archtypes()

def load_archtypes(filename=None):
    global current_set
    global loaded_set

    current_set = Archtype.Archtypes()

    if filename == None:
        filename = app_config.file_path + app_config.filename

    tree = ET.parse(filename)
    data_root = tree.getroot()

    for archtype in data_root:
        current_archtype = Archtype.Archtype(archtype.find('name').text,archtype.find('shortDescription').text)
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

    loaded_set = current_set.clone()

def get_loaded_set():
    global loaded_set

    return loaded_set

if __name__ == '__main__':

    load_archtypes()
    archtype_list()
