import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import GUI_List
import GUI_Race
import Race

list_window = None

def save_race(idx,race):
    global current_set
    global list_window

    current_set.update(idx,race)

    if list_window != None:
        GUI_List.build_list("Races",current_set.get_list(),launch_edit_race, remove_race)

def save_races(filename=None,backup_filename=None):
    global current_set

    data=ET.Element('races')
    for item in current_set:
        r=ET.SubElement(data,'race')
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

def remove_race(idx):
    global current_set

    current_set.remove(current_set[idx])

def launch_edit_race(parent,idx,supress_gui=False):
    global current_set
    global race_window

    race_window = None

    if race_window == None or not Toplevel.winfo_exists(race_window):
        race_window,race_form = GUI_Race.create_race_form(parent)

    if supress_gui:
        return race_window
    else:
        GUI_Race.load_data(current_set[idx],save_race, idx)
        race_window.mainloop()

def launch_race_list(supress_gui=False):
    global current_set
    global loaded_set
    global list_window

    if list_window == None or not Toplevel.winfo_exists(list_window):
        list_window,list_form = GUI_List.create_list_form(None)

    if supress_gui:
        return list_window
    else:
        GUI_List.build_list("Races",current_set.get_list(),launch_edit_race,remove_race)
        list_window.mainloop()
        if not current_set.equals(loaded_set):
            save_race()

def load_race(filename=None):
    global current_set
    global loaded_set

    current_set = Race.Races()

    if filename == None:
        filename = app_config.file_path + app_config.filename

    tree = ET.parse(filename)
    data_root = tree.getroot()

    for race in data_root:
        current_race = Race.Race(race.find('name').text)
        current_race.description = race.find('description').text
        current_race.proficiency = race.find('proficiency').text
        current_race.str_bonus = race.find('strBonus').text
        current_race.per_bonus = race.find('perBonus').text
        current_race.int_bonus = race.find('intBonus').text
        current_race.dex_bonus = race.find('dexBonus').text
        current_race.cha_bonus = race.find('chaBonus').text
        current_race.vit_bonus = race.find('vitBonus').text
        current_race.mag_bonus = race.find('magBonus').text
        current_race.stamina_bonus = race.find('staminaBonus').text
        current_race.attack_bonus = race.find('attackBonus').text
        current_race.reflex_bonus = race.find('reflexBonus').text
        current_race.feats = race.find('feats').text
        current_race.movement = race.find('movement').text
        current_race.skill_points = race.find('skillPoints').text
        current_race.level_health = race.find('levelHealth').text
        current_set.add_new(current_race)

    loaded_set = current_set.clone()

def get_loaded_set():
    global loaded_set

    return loaded_set

if __name__ == '__main__':

    load_races()
    launch_race_list()
