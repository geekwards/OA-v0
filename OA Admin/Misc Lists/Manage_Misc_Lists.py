import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import GUI_List
import GUI_Misc_List
import List_Object

list_window = None

def save_misc_list(idx,misc_list):
    global current_set
    global list_window

    current_set.update(idx,misc_list)

    if list_window != None:
        GUI_List.build_list("Misc Lists",current_set.get_list(),launch_edit_misc_list, remove_misc_list)

def save_misc_list(filename=None,backup_filename=None):
    global current_set

    data=ET.Element('misc_lists')
    for item in current_set:
        r=ET.SubElement(data,'misc_list')
        ET.SubElement(r,'name').text = item.name
        ET.SubElement(r,'description').text = item.description
        ET.SubElement(r,'proficiency').text = item.proficiency
        ET.SubElement(r,'strBonus').text = item.str_bonus
        ET.SubElement(r,'perBonus').text = item.per_bonus
        ET.SubElement(r,'intBonus').text = item.int_bonus
        ET.SubElement(r,'dexBonus').text = item.dex_bonus
        ET.SubElement(r,'chaBonus').text = item.cha_bonus
        ET.SubElement(r,'vitBonus').text = item.vit_bonus
        ET.SubElement(r,'magBonus').text = item.mag_bonus
        ET.SubElement(r,'staminaBonus').text = item.stamina_bonus
        ET.SubElement(r,'attackBonus').text = item.attack_bonus
        ET.SubElement(r,'reflexBonus').text = item.reflex_bonus
        ET.SubElement(r,'feats').text = item.feats
        ET.SubElement(r,'movement').text = item.movement
        ET.SubElement(r,'skillPoints').text = item.skill_points
        ET.SubElement(r,'levelHealth').text = item.level_health

    if filename == None:
        filename = app_config.file_path + app_config.filename

    if backup_filename == None:
        backup_filename = app_config.backup_file_path + app_config.backup_filename

    copy2(filename,backup_filename)
    f = open(filename,'w')
    f.write(ET.tostring(data, encoding="unicode"))
    f.close()

def remove_misc_list(idx):
    global current_set

    current_set.remove(current_set[idx])

def launch_edit_misc_list(parent,idx,supress_gui=False):
    global current_set
    global misc_list_window

    misc_list_window = None

    if misc_list_window == None or not Toplevel.winfo_exists(misc_list_window):
        misc_list_window,misc_list_form = GUI_Misc_List.create_misc_list_form(parent)

    if supress_gui:
        return misc_list_window
    else:
        GUI_Misc_List.load_data(current_set[idx],save_misc_list, idx)
        misc_list_window.mainloop()

def launch_misc_list_list(supress_gui=False):
    global current_set
    global loaded_set
    global list_window

    if list_window == None or not Toplevel.winfo_exists(list_window):
        list_window,list_form = GUI_List.create_list_form(None)

    if supress_gui:
        return list_window
    else:
        GUI_List.build_list("Misc Lists",current_set,launch_edit_misc_list,remove_misc_list)
        list_window.mainloop()
        if not current_set.equals(loaded_set):
            save_misc_list()

def load_misc_list(filename=None):
    global current_set
    global loaded_set

    current_set = []

    if filename == None:
        filename = app_config.file_path + app_config.misc_list_filename

    tree = ET.parse(filename)
    data_root = tree.getroot()

    for misc_list in data_root:
        current_set.append(misc_list)

    loaded_set = current_set.copy()

def get_loaded_set():
    global loaded_set

    return loaded_set

if __name__ == '__main__':

    load_misc_list()
    launch_misc_list_list()
